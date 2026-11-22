# Rapport de vérification — Guide d'initialisation

**Date** : 2026-11-22
**Objet** : preuves brutes du guide, du bootstrap et de l'état du dépôt.

## 1. Historique et état du dépôt

### `git log --oneline -5`

```text
d65ad38 docs: configurer le remote optima-flash et cibler l'URL dans le guide
5c68fd7 docs: guide d'initialisation pour agent et script de bootstrap
471479c chore: initial import — phase 2 validée (socle applicatif)
```

### `git status`

```text
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

### `git remote -v`

```text
origin	https://github.com/digitalholding2026-ux/optima-flash.git (fetch)
origin	https://github.com/digitalholding2026-ux/optima-flash.git (push)
```

### `git ls-files docs/`

```text
docs/ARCHITECTURE.md
docs/GUIDE_INITIALISATION.md
docs/LEGAL.md
docs/PROVENANCE.md
docs/RAPPORT_CORRECTION_2.8_2.9.md
docs/RAPPORT_GUIDE_INIT.md
docs/RAPPORT_PHASE2.md
docs/RAPPORT_PROVENANCE.md
docs/RAPPORT_TRANSPOSITION.md
docs/RAPPORT_VERIFICATION_2.10.md
docs/SPEC.md
docs/STACK.md
```

### `git ls-files scripts/`

```text
scripts/.gitkeep
scripts/bootstrap.ps1
scripts/install_drivers.ps1
```

### `git log origin/master..master --oneline`

```text
```

## 2. Validation syntaxique

Commande exacte fournie :

```text
SYNTAX OK
powershell : [ref] cannot be applied to a variable that does not exist.
At line:1 char:5
+ & { $null = [System.Management.Automation.Language.Parser]::ParseFile ...
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : InvalidOperation: (errors:VariablePath) [RuntimeException], RuntimeException
+ FullyQualifiedErrorId : NonExistingVariableReference
```

La commande ne déclare pas `$errors` avant `[ref]$errors`. Après `$errors = $null` :

```text
SYNTAX OK
```

Ce n'est pas un défaut du script.

## 3. Contenu du guide

`Get-Content docs/GUIDE_INITIALISATION.md | Measure-Object -Line` :

```text
Lines Words Characters Property
----- ----- ---------- --------
  107
```

`Select-String -Pattern "^## "` :

```text
6: ## 1. Prérequis machine
18: ## 2. Clone et installation
44: ## 3. Backend USB (étape manuelle critique)
59: ## 4. Pilotes USB appareils
99: ## 5. Vérification de l'environnement
123: ## 6. Lecture du contexte projet (obligatoire)
136: ## 7. Règles de travail
147: ## 8. État du projet et prochaine étape
```

SHA-256 :

```text
F9A76EA1D7AD963AC1C075FDA0099C6EF52E79DB82453884A0EF29D102EBA1AE
```

## 4. Verdict

**GUIDE VALIDÉ — PRÊT POUR 3.1**