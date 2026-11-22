# Guide d'initialisation — Optima Telecom Flash Tool

**Public** : agent technique qui clone le dépôt sur une machine neuve.
**Avant de coder** : lire les 6 documents de la section 6.

## 1. Prérequis machine

| Élément | Commande | Sortie attendue |
|---|---|---|
| Windows 10/11 x64 | — | — |
| Python 3.11.x exact | `py -3.11 --version` | `Python 3.11.9` |
| Git | `git --version` | `git version 2.xx.x` |
| Droits admin | — | pour `scripts/install_drivers.ps1` |
| Réseau | `git clone`, `pip install` | accès au dépôt et à PyPI |

Si `py -3.11` n'est pas reconnu, installer Python 3.11.x depuis python.org et cocher « Add python.exe to PATH ».

## 2. Clone et installation

```powershell
git clone https://github.com/digitalholding2026-ux/optima-flash.git
cd optima-flash
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

Sortie attendue (fin) :

```text
Successfully installed PySide6-6.12.0 ... optima-flash-0.1.0 ...
```

Si `Activate.ps1` est bloqué par la stratégie d'exécution :

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

Ou appeler directement `.venv\Scripts\python.exe` sans activer le venv.

## 3. Backend USB (étape manuelle critique)

1. Télécharger l'archive officielle sur <https://libusb.info/> (libusb 1.0.x, Windows).
2. Extraire `libusb-1.0.dll` **x64** (dossier `x64` ou `MS64`).
3. Copier la DLL dans `.venv\Scripts\` (à côté de `python.exe`).
4. Vérifier :

```powershell
python -c "import usb.core; print(usb.core.find(find_all=True))"
```

Sortie attendue : `[]` (aucun `NoBackendError`).

**Non automatisable** : aucune DLL n'est versionnée dans le dépôt ; aucun téléchargement automatique. Si `NoBackendError` persiste, vérifier que `libusb-1.0.dll` est bien dans `.venv\Scripts\` et qu'elle est x64.

## 4. Pilotes USB appareils

Exécuter en administrateur :

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install_drivers.ps1
```

**Rôle** : guider l'installation des pilotes MediaTek preloader / Qualcomm EDL 9008 et du backend libusb.

**Ce qu'il fait** :
- vérifie les droits admin ;
- crée `drivers/` ;
- cherche `libusb-1.0.dll` dans `drivers/` et `System32` ;
- affiche les commandes `pnputil /add-driver "<inf>" /install` ;
- affiche un avertissement signature (jamais exécuté) ;
- rappelle : redémarrer, rebrancher, relancer Optima.

**Ce qu'il ne fait pas** : aucun téléchargement, aucune installation automatique, aucune désactivation de signature.

**Confirmation attendue** : `Droits administrateur : OK`, puis la liste des `.inf` et les commandes `pnputil`.

**Vérification** :

```powershell
python -c "from src.adapters.usb.drivers import check_drivers; print(check_drivers())"
```

Sortie attendue :

```text
{'mtk_vcom': True, 'qualcomm_9008': True, 'libusb_backend': True}
```

Si un `False` persiste :
- `libusb_backend: False` → copier `libusb-1.0.dll` dans `.venv\Scripts\` (section 3).
- `mtk_vcom: False` → brancher l'appareil en preloader, installer l `.inf` MediaTek via `pnputil`.
- `qualcomm_9008: False` → brancher en EDL 9008, installer l `.inf` Qualcomm.
- Après installation : redémarrer, rebrancher, relancer la commande.

## 5. Vérification de l'environnement

Dans l'ordre, depuis la racine du dépôt :

```powershell
python -m pytest
python -m mypy --strict src/core src/adapters src/ui
python -m ruff check src tests
pip-licenses --fail-on="GPL"
```

Sorties attendues :

```text
35 passed
Success: no issues found in 15 source files
All checks passed!
# table des licences, exit code 0
```

Automatisation : `powershell -ExecutionPolicy Bypass -File scripts\bootstrap.ps1` (les 4 contrôles). `-SkipLint` limite à pytest + pip-licenses. Le script ne crée pas le venv, ne télécharge rien, n'installe pas les pilotes.

Tout doit passer avant de continuer.

## 6. Lecture du contexte projet (obligatoire)

Ordre imposé :

1. `docs/SPEC.md` — périmètre MVP, 5 fonctionnalités prioritaires, 3 exclusions.
2. `docs/ARCHITECTURE.md` — isolation GPL par sous-processus, ADR-001/ADR-002.
3. `docs/LEGAL.md` — FRP propriétaire légitime, preuve écrite, audit, RGPD.
4. `docs/STACK.md` — Python 3.11+, PySide6, pyusb/libusb, SQLite.
5. `docs/PROVENANCE.md` — antériorité v0.5, réécriture indépendante, convention MainWindow.
6. `docs/RAPPORT_TRANSPOSITION.md` — similarité 3,67 %, aucune signature PyQt5 résiduelle.

**Ne pas coder avant d'avoir lu les 6.**

## 7. Règles de travail

1. Un prompt = 3 à 4 éléments maximum, jamais tout à la fois.
2. Aucune dépendance GPL dans `src/` (`pip-licenses --fail-on="GPL"`).
3. `mtkclient` et `edl` uniquement en sous-processus, jamais d'import.
4. Aucun binaire versionné (`.dll`, `.exe`, `.pyd`).
5. Aucun appel réseau dans `src/`.
6. Aucune écriture USB hors des méthodes d'adaptateur prévues.
7. Type hints complets ; `mypy --strict` doit passer.
8. Toute opération sensible produit une entrée d'audit append-only (jamais de `UPDATE`/`DELETE`) — à venir en phase 3+.

## 8. État du projet et prochaine étape

> Phase 2 validée (socle applicatif), commit `471479c`. Phase 3 en cours : contrat CLI mtkclient (`docs/CONTRAT_CLI_MTKCLIENT.md`) puis `core/runner.py`, puis `adapters/mtk/detect()` et `read_info()`.

Dernier rapport de phase : `docs/RAPPORT_TRANSPOSITION.md` (et `docs/RAPPORT_PROVENANCE.md`). `docs/CONTRAT_CLI_MTKCLIENT.md` n'existe pas encore : il sera créé au prompt 3.