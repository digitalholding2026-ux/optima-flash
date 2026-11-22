# Rapport de vérification — runner (prompt 3.2)

**Périmètre** : `src/core/runner.py`, `tests/test_runner.py`. Aucune modification, aucune correction.
**Date** : 2026-11-22. **Plateforme** : Windows, Python 3.11.9 (`.venv`).

## 1. Sécurité du runner — greps bruts

### `Select-String -Path src/core/runner.py -Pattern "shell"`

```
10: * ``shell=False`` obligatoire, aucune chaîne de commande concaténée ;
115:     """Exécute ``cmd`` sans shell et retourne sa sortie texte.
117:     :param cmd: argv complet ; ``cmd[0]`` est le binaire, jamais une ligne shell.
138:         shell=False,
```

Écart constaté : le motif `shell` apparaît aussi dans la docstring (lignes 10, 115, 117). La seule occurrence de code exécutable est la ligne 138 : `shell=False,`.

### `Select-String -Path src/core/runner.py -Pattern "^\s*print\("`

```
(vide)
```

### `Select-String -Path src/core/runner.py -Pattern "import (mtkclient|edl|usb)|from (mtkclient|edl|usb)"`

```
(vide)
```

### `Select-String -Path src/core/runner.py -Pattern "import (socket|requests|urllib)"`

```
(vide)
```

### `git diff HEAD~1 -- pyproject.toml`

```
git : The term 'git' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:4 char:38
+ Write-Output "=== A6: git diff ==="; git diff HEAD~1 -- pyproject.tom ...
+                                      ~~~ CategoryInfo          : ObjectNotFound: (git:String) [], CommandNotFoundException
+ FullyQualifiedErrorId : CommandNotFoundException
```

Écart constaté : `git` est absent du PATH ; le diff ne peut pas être produit. Contrôle de substitution sur le contenu du fichier :

```
13: dependencies = [
14: "PySide6>=6.6,<7",
15: "pyusb>=1.2,<2",
16: "pyyaml>=6,<7",
19: [project.optional-dependencies]
21: "pytest",
22: "pytest-qt",
23: "ruff",
24: "mypy",
```

### `Get-Content src/core/runner.py | Measure-Object -Line`

```
198
```

## 2. Couverture des 8 tests — `pytest -v` brut

Commande demandée : `.\.venv\Scripts\python.exe -m pytest tests/test_runner.py -v`

```
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.2.0, pluggy-1.7.0
PySide6 6.12.0 -- Qt runtime 6.12.0 -- Qt compiled 6.12.0
rootdir: C:\Users\Docker\Desktop\optima-flash
configfile: pyproject.toml
plugins: qt-4.5.0
collected 8 items

tests\test_runner.py ........                                            [100%]

============================== 8 passed in 1.63s ==============================
```

Écart constaté : `-q` est présent dans `addopts` (`pyproject.toml`), la sortie agrégée ne liste pas les noms. Relance avec `addopts` neutralisé (`-o addopts=""`), même sélection :

```
tests/test_runner.py::test_success_returns_zero_and_stdout PASSED        [ 12%]
tests/test_runner.py::test_nonzero_returncode_does_not_raise PASSED      [ 25%]
tests/test_runner.py::test_timeout_kills_process PASSED                  [ 37%]
tests/test_runner.py::test_cancel_event_kills_process PASSED             [ 50%]
tests/test_runner.py::test_text_decoding_is_utf8 PASSED                  [ 62%]
tests/test_runner.py::test_missing_binary_raises_file_not_found PASSED   [ 75%]
tests/test_runner.py::test_to_operation_result_success PASSED            [ 87%]
tests/test_runner.py::test_to_operation_result_timeout PASSED            [100%]

============================== 8 passed in 1.72s ==============================
```

Correspondance attendu / obtenu :

| Attendu | Test | Statut |
|---|---|---|
| succès | `test_success_returns_zero_and_stdout` | PASSED |
| échec returncode 3 | `test_nonzero_returncode_does_not_raise` | PASSED |
| timeout réel < 2000 ms | `test_timeout_kills_process` | PASSED |
| annulation `cancel_event` | `test_cancel_event_kills_process` | PASSED |
| encodage éàü | `test_text_decoding_is_utf8` | PASSED |
| FileNotFoundError | `test_missing_binary_raises_file_not_found` | PASSED |
| `to_operation_result` succès | `test_to_operation_result_success` | PASSED |
| `to_operation_result` timeout | `test_to_operation_result_timeout` | PASSED |

## 3. Preuve de kill effectif (timeout / annulation)

### Corps des tests — `Get-Content tests/test_runner.py | Select-String -Pattern "timeout|annul|cancel" -Context 3,3`

```
--- line 34 ---
  assert sr.cancelled is False


def test_timeout_kills_process() -> None:
>     sr = run_subprocess(_python("-c", "import time; time.sleep(5)"), timeout_s=0.5)

  assert sr.timed_out is True
  assert sr.returncode is None
```

```
--- line 42 ---
  assert sr.duration_ms < 2000


def test_cancel_event_kills_process() -> None:
>     event = threading.Event()
  threading.Timer(0.2, event.set).start()

  sr = run_subprocess(_python("-c", "import time; time.sleep(5)"), cancel_event=event)

  assert sr.cancelled is True
  assert sr.timed_out is False
  assert sr.returncode is None
  assert sr.duration_ms < 2000
```

### Mesure hors pytest — `Measure-Command`

```
Measure-Command TotalSeconds: 0,73103
Measure-Command TotalMilliseconds: 731,03
```

`Measure-Command` ne restitue pas la sortie du bloc ; capture complémentaire de la sortie interne (chronomètre autour du même appel) :

```
SORTIE: True None 530
MESURE: 866 ms
```

`True None 530` = `timed_out=True`, `returncode=None`, `duration_ms=530` (< 2000). Mesure totale 866 ms (< 2 s).

RUNNER CONFIRMÉ — PRÊT POUR 3.3