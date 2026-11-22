# Rapport de transposition PyQt5 → PySide6

**Date** : 2026-11-22
**Objet** : vérifier qu'aucun code PyQt5 du projet v5 (`12a505c`) n'a été transposé mécaniquement vers PySide6.
**Méthode** : `git show`, `git grep`, script `difflib` éphémère (hors dépôt), aucune modification de `src/`.

## 1. Cartographie des correspondances fonctionnelles

Le prompt mentionne 7 fichiers source ; `src/` en contient en réalité **9 non vides** (hors `__init__.py`).

| Fichier actuel | Rôle fonctionnel | Fichiers `12a505c` candidats |
|---|---|---|
| `src/core/types.py` | Enums, dataclasses | `core/device_models.py`, `core/__init__.py` |
| `src/core/config.py` | Configuration | `core/init_env.py` |
| `src/core/logging.py` | Journalisation | aucun module dédié ; plus proche `gui/log_panel.py` (panneau UI) |
| `src/core/license.py` | Placeholder licence | **aucun dans `12a505c`** (système ajouté après : `f8d3d0d`, `b883e8e`, `7f7822c`) |
| `src/adapters/usb/detector.py` | Détection USB | `core/detector.py`, `core/usb_scanner.py` |
| `src/adapters/usb/drivers.py` | Diagnostic pilotes | `core/com_detector.py` |
| `src/adapters/mtk/adapter.py` | Stub MTK | `core/actions.py`, `core/mtk_communication.py` |
| `src/adapters/qualcomm/adapter.py` | Stub Qualcomm | **aucun** (v5 est centré MediaTek ; seul `core/usb_scanner.py` mentionne 9008/Qualcomm) |
| `src/ui/main_window.py` | Fenêtre principale | `gui/main_window.py` |

**Fichiers `12a505c` sans correspondance dans `src/`** : `audit_usb.py`, `build_exe.py`, `build.bat`, `build_installer.bat`, `installer.iss`, `install.bat`, `install_dependencies.ps1`, `OptimaMTKTool.spec`, `core/actions.py`, `core/brom/handshake.py`, `core/usb_reset.py`, `main.py`, et les onglets `gui/connection_assistant.py`, `dashboard.py`, `device_info_tab.py`, `device_status_widget.py`, `flash_tab.py`, `frp_tab.py`, `log_panel.py`, `tft_widgets.py`, `tools_tab.py`. Ces zones sont soit du build/packaging, soit des fonctions métier non implémentées à ce stade.

## 2. Similarité textuelle normalisée

Normalisation : suppression des lignes vides et des commentaires `#`, puis `difflib.SequenceMatcher` ligne-à-ligne. Script éphémère hors dépôt.

```text
Fichier actuel | Fichier v5 | Ratio | Nb séquences >=3 | Nb identifiants partagés
src/core/types.py | core/device_models.py | 1.22% | 0 | 0
src/core/types.py | core/__init__.py | 0.78% | 0 | 0
src/core/config.py | core/init_env.py | 2.48% | 0 | 0
src/core/logging.py | gui/log_panel.py | 0.95% | 0 | 0
src/adapters/usb/detector.py | core/detector.py | 1.10% | 0 | 0
src/adapters/usb/detector.py | core/usb_scanner.py | 2.49% | 0 | 0
src/adapters/usb/drivers.py | core/com_detector.py | 3.67% | 0 | 0
src/adapters/mtk/adapter.py | core/actions.py | 0.26% | 0 | 1
  identifiants partagés: ['erase_frp']
src/adapters/mtk/adapter.py | core/mtk_communication.py | 1.05% | 0 | 0
src/ui/main_window.py | gui/main_window.py | 1.52% | 0 | 3
  identifiants partagés: ['MainWindow', '__init__', 'closeEvent']
```

Aucune paire n'atteint 10 % ; aucune séquence de 3 lignes identiques. Les seuls identifiants partagés sont `erase_frp` (terme métier du SPEC) et `MainWindow`, `__init__`, `closeEvent` (noms génériques Qt).

## 3. Transposition PyQt5 → PySide6

### 3.1 Occurrences PyQt5 dans `12a505c` (brut, trié par fréquence)

```text
12a505c:build/OptimaMTKTool/Analysis-00.toc:230
12a505c:build/OptimaMTKTool/COLLECT-00.toc:228
12a505c:dist/OptimaMTKTool/_internal/PyQt5/QtWidgets.pyd:97
12a505c:build/OptimaMTKTool/xref-OptimaMTKTool.html:80
12a505c:dist/OptimaMTKTool/_internal/PyQt5/QtGui.pyd:60
12a505c:dist/OptimaMTKTool/_internal/PyQt5/QtCore.pyd:40
12a505c:gui/flash_tab.py:4
12a505c:main.py:4
12a505c:gui/device_info_tab.py:3
12a505c:gui/dashboard.py:3
12a505c:gui/connection_assistant.py:3
12a505c:gui/main_window.py:3
12a505c:gui/tft_widgets.py:3
12a505c:gui/tools_tab.py:3
12a505c:gui/device_status_widget.py:3
12a505c:gui/frp_tab.py:3
12a505c:gui/log_panel.py:3
12a505c:README.md:2
12a505c:requirements.txt:1
12a505c:core/mtk_communication.py:1
12a505c:core/detector.py:1
```

Les artefacts de build/dist concentrent les occurrences ; les fichiers source en ont 1 à 4.

### 3.2 `grep -R "PyQt5" src/`

```text
EXIT=1
```

Aucune sortie : aucune référence PyQt5 dans le code actuel.

### 3.3 Signatures caractéristiques

| Signature | `12a505c` | `src/` actuel |
|---|---|---|
| `pyqtSignal` | `core/detector.py:21,336-340,1176-1179`, `core/mtk_communication.py:9,17-19`, `gui/frp_tab.py:14,37-39`, `gui/tft_widgets.py:18,48,130,355,627`, `gui/tools_tab.py:18,41-43` | `Signal` : `src/ui/main_window.py:11,43-44,62-63` |
| `pyqtSlot` | `gui/device_status_widget.py:11,83`, `gui/main_window.py:19` | `Slot` : `src/ui/main_window.py:11,46,65,191,215,225,231,235,257,295,300` |
| `QApplication.exec_()` | `gui/connection_assistant.py:335`, `main.py:158` | `exec()` : `src/ui/main_window.py:283,317` |
| `setWindowIcon(QIcon(...))` | `main.py:150` | aucune |
| `from PyQt5.QtCore import *` | aucune | imports explicites |

Les différences `pyqtSignal` → `Signal`, `pyqtSlot` → `Slot`, `exec_()` → `exec()` sont cohérentes avec une réécriture PySide6. Aucune signature PyQt5 ne subsiste dans `src/`. Les noms `MainWindow` et `erase_frp` relèvent du domaine (fenêtre principale, opération FRP du SPEC), pas d'un bloc de code copié.

## 4. Verdict

**TRANSPOSITION MINEURE (inspiration, code réécrit)**

Justification : similarité normalisée maximale de 3.67 %, aucune séquence de 3 lignes identiques, et seuls des identifiants génériques/métier partagés (`MainWindow`, `__init__`, `closeEvent`, `erase_frp`). Les signatures PyQt5 (`pyqtSignal`, `pyqtSlot`, `exec_()`) sont absentes de `src/`, remplacées par leurs équivalents PySide6. Le code actuel est une réécriture PySide6 du même domaine fonctionnel, sans preuve de transposition mécanique.