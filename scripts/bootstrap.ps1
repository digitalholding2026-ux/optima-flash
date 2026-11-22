#Requires -Version 5.1
[CmdletBinding()]
param(
    [switch]$SkipLint
)

$ErrorActionPreference = 'Stop'

function Write-Step {
    param([string]$Message)
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Write-Ok {
    param([string]$Message)
    Write-Host "OK  $Message" -ForegroundColor Green
}

function Write-Fail {
    param([string]$Message)
    Write-Host "ÉCHEC — $Message" -ForegroundColor Red
}

$repoRoot = Split-Path -Parent $PSScriptRoot
Push-Location -LiteralPath $repoRoot

try {
    Write-Step "Vérification de Python"
    $pythonVersion = ""
    $pythonExit = 1
    $previous = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
        if ($pyLauncher) {
            $pythonVersion = (& py -3.11 --version 2>&1 | Out-String).Trim()
            $pythonExit = $LASTEXITCODE
        }
        if ($pythonExit -ne 0 -or $pythonVersion -notmatch "Python 3\.11\.\d+") {
            $pythonVersion = (& python --version 2>&1 | Out-String).Trim()
            $pythonExit = $LASTEXITCODE
        }
    }
    catch {
        $pythonVersion = ""
        $pythonExit = 1
    }
    finally {
        $ErrorActionPreference = $previous
    }
    Write-Host "Python : $pythonVersion"
    if ($pythonExit -ne 0 -or $pythonVersion -notmatch "Python 3\.11\.\d+") {
        Write-Fail "Python 3.11.x requis (py -3.11 ou python --version)"
        exit 1
    }
    Write-Ok "Python 3.11.x"

    Write-Step "Vérification du venv"
    $venvPython = [System.IO.Path]::GetFullPath((Join-Path $repoRoot ".venv\Scripts\python.exe"))
    if (-not (Test-Path -LiteralPath $venvPython)) {
        Write-Fail "Créez d'abord le venv — voir section 2 du guide"
        exit 1
    }
    Write-Ok "Venv trouvé"

    $checks = @()
    $checks += @{ Name = "pytest"; Exe = $venvPython; Args = @("-m", "pytest") }
    if (-not $SkipLint) {
        $checks += @{
            Name = "mypy"
            Exe = $venvPython
            Args = @("-m", "mypy", "--strict", "src/core", "src/adapters", "src/ui")
        }
        $checks += @{
            Name = "ruff"
            Exe = $venvPython
            Args = @("-m", "ruff", "check", "src", "tests")
        }
    }
    $pipLicenses = [System.IO.Path]::GetFullPath(
        (Join-Path $repoRoot ".venv\Scripts\pip-licenses.exe")
    )
    $checks += @{
        Name = "pip-licenses"
        Exe = $pipLicenses
        Args = @("--fail-on=GPL")
    }

    foreach ($check in $checks) {
        Write-Step $check.Name
        $checkArgs = $check.Args
        & $check.Exe @checkArgs
        if ($LASTEXITCODE -ne 0) {
            Write-Fail "$($check.Name) a échoué"
            exit 1
        }
        Write-Ok $check.Name
    }

    Write-Host ""
    Write-Host "OK — environnement prêt pour la phase 3" -ForegroundColor Green
    exit 0
}
finally {
    Pop-Location
}