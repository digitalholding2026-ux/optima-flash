# Rapport de provenance

**Date** : 2026-11-22
**Objet** : relation factuelle entre `src/` actuel et l'arborescence du commit `12a505c`, sans présomption de copie ni de non-copie.
**Méthode** : commandes git brutes, scripts d'analyse éphémères, aucune correction, aucune purge.

## 1. Inventaire des fichiers dans 12a505c

### 1.1 `git ls-tree -r --name-only 12a505c` (brut, sans filtre)

```text
.gitignore
OptimaMTKTool.spec
README.md
__pycache__/audit_usb.cpython-315.pyc
__pycache__/main.cpython-315.pyc
assets/.gitkeep
assets/icon.ico
audit_usb.py
bin/AdbWinApi.dll
bin/AdbWinUsbApi.dll
bin/README.md
bin/adb.exe
bin/fastboot.exe
bin/libusb-1.0.dll
bin/setup_platform_tools.ps1
bin/x64/libusb-1.0.dll
build.bat
build/OptimaMTKTool/Analysis-00.toc
build/OptimaMTKTool/COLLECT-00.toc
build/OptimaMTKTool/EXE-00.toc
build/OptimaMTKTool/OptimaMTKTool.exe
build/OptimaMTKTool/OptimaMTKTool.pkg
build/OptimaMTKTool/PKG-00.toc
build/OptimaMTKTool/PYZ-00.pyz
build/OptimaMTKTool/PYZ-00.toc
build/OptimaMTKTool/base_library.zip
build/OptimaMTKTool/localpycs/pyimod01_archive.pyc
build/OptimaMTKTool/localpycs/pyimod02_importers.pyc
build/OptimaMTKTool/localpycs/pyimod03_ctypes.pyc
build/OptimaMTKTool/localpycs/pyimod04_pywin32.pyc
build/OptimaMTKTool/localpycs/struct.pyc
build/OptimaMTKTool/warn-OptimaMTKTool.txt
build/OptimaMTKTool/xref-OptimaMTKTool.html
build_exe.py
build_installer.bat
core/__init__.py
core/__pycache__/__init__.cpython-315.pyc
core/__pycache__/actions.cpython-315.pyc
core/__pycache__/com_detector.cpython-315.pyc
core/__pycache__/detector.cpython-315.pyc
core/__pycache__/device_models.cpython-315.pyc
core/__pycache__/init_env.cpython-315.pyc
core/__pycache__/mtk_communication.cpython-315.pyc
core/__pycache__/usb_reset.cpython-315.pyc
core/__pycache__/usb_scanner.cpython-315.pyc
core/actions.py
core/brom/__init__.py
core/brom/__pycache__/__init__.cpython-315.pyc
core/brom/__pycache__/handshake.cpython-315.pyc
core/brom/handshake.py
core/com_detector.py
core/detector.py
core/device_models.py
core/init_env.py
core/mtk_communication.py
core/usb_reset.py
core/usb_scanner.py
data/auth/README.md
data/da/README.md
dist/OptimaMTKTool/OptimaMTKTool.exe
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/MSVCP140.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/MSVCP140_1.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Core.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5DBus.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Gui.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Network.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Qml.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5QmlModels.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Quick.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Svg.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5WebSockets.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/Qt5Widgets.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/VCRUNTIME140.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/VCRUNTIME140_1.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/d3dcompiler_47.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/libEGL.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/libGLESv2.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/bin/opengl32sw.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/generic/qtuiotouchplugin.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/iconengines/qsvgicon.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qgif.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qicns.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qico.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qjpeg.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qsvg.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qtga.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qtiff.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qwbmp.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/imageformats/qwebp.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/platforms/qminimal.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/platforms/qoffscreen.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/platforms/qwebgl.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/platforms/qwindows.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/platformthemes/qxdgdesktopportal.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/plugins/styles/qwindowsvistastyle.dll
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_ar.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_bg.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_ca.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_cs.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_da.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_de.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_en.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_es.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_fa.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_fi.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_fr.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_gd.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_gl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_he.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_ar.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_bg.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_ca.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_cs.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_da.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_de.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_en.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_es.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_fr.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_gl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_hu.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_it.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_ja.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_ko.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_pl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_ru.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_sk.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_sl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_tr.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_uk.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_zh_CN.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_help_zh_TW.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_hu.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_it.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_ja.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_ko.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_lt.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_lv.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_pl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_pt.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_ru.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_sk.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_sl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_sv.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_tr.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_uk.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_zh_CN.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qt_zh_TW.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_ar.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_bg.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_ca.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_cs.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_da.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_de.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_en.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_es.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_fi.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_fr.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_gd.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_he.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_hu.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_it.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_ja.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_ko.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_lv.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_pl.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_ru.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_sk.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_tr.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_uk.qm
dist/OptimaMTKTool/_internal/PyQt5/Qt5/translations/qtbase_zh_TW.qm
dist/OptimaMTKTool/_internal/PyQt5/QtCore.pyd
dist/OptimaMTKTool/_internal/PyQt5/QtGui.pyd
dist/OptimaMTKTool/_internal/PyQt5/QtWidgets.pyd
dist/OptimaMTKTool/_internal/PyQt5/sip.cp315-win_amd64.pyd
dist/OptimaMTKTool/_internal/VCRUNTIME140.dll
dist/OptimaMTKTool/_internal/VCRUNTIME140_1.dll
dist/OptimaMTKTool/_internal/_bz2.pyd
dist/OptimaMTKTool/_internal/_ctypes.pyd
dist/OptimaMTKTool/_internal/_decimal.pyd
dist/OptimaMTKTool/_internal/_hashlib.pyd
dist/OptimaMTKTool/_internal/_lzma.pyd
dist/OptimaMTKTool/_internal/_multiprocessing.pyd
dist/OptimaMTKTool/_internal/_queue.pyd
dist/OptimaMTKTool/_internal/_socket.pyd
dist/OptimaMTKTool/_internal/_ssl.pyd
dist/OptimaMTKTool/_internal/_wmi.pyd
dist/OptimaMTKTool/_internal/_zstd.pyd
dist/OptimaMTKTool/_internal/assets/.gitkeep
dist/OptimaMTKTool/_internal/assets/icon.ico
dist/OptimaMTKTool/_internal/base_library.zip
dist/OptimaMTKTool/_internal/bin/AdbWinApi.dll
dist/OptimaMTKTool/_internal/bin/AdbWinUsbApi.dll
dist/OptimaMTKTool/_internal/bin/README.md
dist/OptimaMTKTool/_internal/bin/adb.exe
dist/OptimaMTKTool/_internal/bin/fastboot.exe
dist/OptimaMTKTool/_internal/bin/libusb-1.0.dll
dist/OptimaMTKTool/_internal/bin/setup_platform_tools.ps1
dist/OptimaMTKTool/_internal/bin/x64/libusb-1.0.dll
dist/OptimaMTKTool/_internal/data/auth/README.md
dist/OptimaMTKTool/_internal/data/da/README.md
dist/OptimaMTKTool/_internal/drivers/README.md
dist/OptimaMTKTool/_internal/drivers/adb_fastboot/android_winusb.inf
dist/OptimaMTKTool/_internal/drivers/install_drivers.bat
dist/OptimaMTKTool/_internal/drivers/install_drivers.ps1
dist/OptimaMTKTool/_internal/drivers/libusb_filter/mtk_brom_filter.inf
dist/OptimaMTKTool/_internal/drivers/vcom/cdc-acm.inf
dist/OptimaMTKTool/_internal/libcrypto-3.dll
dist/OptimaMTKTool/_internal/libffi-8.dll
dist/OptimaMTKTool/_internal/libssl-3.dll
dist/OptimaMTKTool/_internal/libusb-1.0.dll
dist/OptimaMTKTool/_internal/pyexpat.pyd
dist/OptimaMTKTool/_internal/python3.dll
dist/OptimaMTKTool/_internal/python315.dll
dist/OptimaMTKTool/_internal/select.pyd
dist/OptimaMTKTool/_internal/setuptools/_vendor/jaraco/text/Lorem ipsum.txt
dist/OptimaMTKTool/_internal/unicodedata.pyd
dist/OptimaMTKTool/bin/AdbWinApi.dll
dist/OptimaMTKTool/bin/AdbWinUsbApi.dll
dist/OptimaMTKTool/bin/README.md
dist/OptimaMTKTool/bin/adb.exe
dist/OptimaMTKTool/bin/fastboot.exe
dist/OptimaMTKTool/bin/libusb-1.0.dll
dist/OptimaMTKTool/bin/setup_platform_tools.ps1
dist/OptimaMTKTool/bin/x64/libusb-1.0.dll
dist/OptimaMTKTool/data/auth/README.md
dist/OptimaMTKTool/data/da/README.md
dist/OptimaMTKTool/drivers/README.md
dist/OptimaMTKTool/drivers/adb_fastboot/android_winusb.inf
dist/OptimaMTKTool/drivers/install_drivers.bat
dist/OptimaMTKTool/drivers/install_drivers.ps1
dist/OptimaMTKTool/drivers/libusb_filter/mtk_brom_filter.inf
dist/OptimaMTKTool/drivers/vcom/cdc-acm.inf
dist/OptimaMTKTool/libusb-1.0.dll
drivers/README.md
drivers/adb_fastboot/android_winusb.inf
drivers/install_drivers.bat
drivers/install_drivers.ps1
drivers/libusb_filter/mtk_brom_filter.inf
drivers/vcom/cdc-acm.inf
gui/__init__.py
gui/__pycache__/__init__.cpython-315.pyc
gui/__pycache__/connection_assistant.cpython-315.pyc
gui/__pycache__/dashboard.cpython-315.pyc
gui/__pycache__/device_info_tab.cpython-315.pyc
gui/__pycache__/device_status_widget.cpython-315.pyc
gui/__pycache__/flash_tab.cpython-315.pyc
gui/__pycache__/frp_tab.cpython-315.pyc
gui/__pycache__/log_panel.cpython-315.pyc
gui/__pycache__/main_window.cpython-315.pyc
gui/__pycache__/tft_widgets.cpython-315.pyc
gui/__pycache__/tools_tab.cpython-315.pyc
gui/connection_assistant.py
gui/dashboard.py
gui/device_info_tab.py
gui/device_status_widget.py
gui/flash_tab.py
gui/frp_tab.py
gui/log_panel.py
gui/main_window.py
gui/tft_widgets.py
gui/tools_tab.py
install.bat
install_dependencies.ps1
installer.iss
main.py
path/to/filename.js
redist/VC_redist.x64.exe
requirements.txt
tools/AdbWinApi.dll
tools/AdbWinUsbApi.dll
tools/README.txt
tools/adb.exe
tools/fastboot.exe
tools/libusb-1.0.dll
```

### 1.2 Fichiers Python source (26) — taille en octets

| Fichier | Octets |
|---|---:|
| `audit_usb.py` | 13244 |
| `build_exe.py` | 4272 |
| `core/__init__.py` | 1612 |
| `core/actions.py` | 42821 |
| `core/brom/__init__.py` | 594 |
| `core/brom/handshake.py` | 4163 |
| `core/com_detector.py` | 698 |
| `core/detector.py` | 51591 |
| `core/device_models.py` | 12077 |
| `core/init_env.py` | 13169 |
| `core/mtk_communication.py` | 8274 |
| `core/usb_reset.py` | 16567 |
| `core/usb_scanner.py` | 18379 |
| `gui/__init__.py` | 847 |
| `gui/connection_assistant.py` | 14117 |
| `gui/dashboard.py` | 13877 |
| `gui/device_info_tab.py` | 14538 |
| `gui/device_status_widget.py` | 6996 |
| `gui/flash_tab.py` | 9833 |
| `gui/frp_tab.py` | 17546 |
| `gui/log_panel.py` | 6213 |
| `gui/main_window.py` | 23739 |
| `gui/tft_widgets.py` | 36181 |
| `gui/tools_tab.py` | 23515 |
| `main.py` | 6263 |

### 1.3 Autres fichiers (248) — synthèse par catégorie

| Catégorie | Nombre | Exemples |
|---|---:|---|
| `dist/OptimaMTKTool/` (PyInstaller) | ~200 | `PyQt5/Qt5/bin/*.dll`, `translations/*.qm`, `_internal/*.pyd` |
| `build/OptimaMTKTool/` | 14 | `*.toc`, `*.exe`, `*.pkg`, `*.pyz`, `xref-*.html` |
| `bin/` | 8 | `adb.exe`, `fastboot.exe`, `libusb-1.0.dll`, `AdbWinApi.dll`, `setup_platform_tools.ps1` |
| `tools/` | 6 | `adb.exe`, `fastboot.exe`, `libusb-1.0.dll`, `AdbWinApi.dll` |
| `drivers/` | 6 | `install_drivers.ps1`, `adb_fastboot/android_winusb.inf`, `vcom/cdc-acm.inf` |
| `data/` | 2 | `auth/README.md`, `da/README.md` |
| `assets/` | 2 | `icon.ico`, `.gitkeep` |
| `redist/` | 1 | `VC_redist.x64.exe` |
| Racine | 10 | `.gitignore`, `OptimaMTKTool.spec`, `README.md`, `installer.iss`, `requirements.txt`… |
| `__pycache__/` | 2 + 9 + 11 | `.pyc` dans `__pycache__/`, `core/__pycache__/`, `gui/__pycache__/` |

La liste brute complète figure en 1.1.

## 2. Similarité avec `src/` actuel

Script `difflib.SequenceMatcher` ligne-à-ligne ; seuils utilisés : **Copie ≥ 60 %**, **Inspiration 10–60 %** (ou bloc partagé significatif), **Indépendant < 10 %**.

| Fichier `src/` | Fichier `12a505c` correspondant | Similarité | Verdict |
|---|---|---:|---|
| `src/__init__.py` | `core/__init__.py` | 0.00 % | Indépendant (fichier vide) |
| `src/adapters/__init__.py` | `core/__init__.py` | 0.00 % | Indépendant (fichier vide) |
| `src/adapters/mtk/__init__.py` | `core/__init__.py` | 0.00 % | Indépendant (fichier vide) |
| `src/adapters/mtk/adapter.py` | — | — | Indépendant (aucun nom identique) |
| `src/adapters/qualcomm/__init__.py` | `core/__init__.py` | 0.00 % | Indépendant (fichier vide) |
| `src/adapters/qualcomm/adapter.py` | — | — | Indépendant (aucun nom identique) |
| `src/adapters/usb/__init__.py` | `core/__init__.py` | 6.15 % | Indépendant (aucun bloc ≥ 3 lignes) |
| `src/adapters/usb/detector.py` | `core/detector.py` | 2.34 % | Indépendant (aucun bloc ≥ 3 lignes) |
| `src/adapters/usb/drivers.py` | — | — | Indépendant (aucun nom identique) |
| `src/core/__init__.py` | `core/__init__.py` | 0.00 % | Indépendant (fichier vide) |
| `src/core/config.py` | — | — | Indépendant (aucun nom identique) |
| `src/core/license.py` | — | — | Indépendant (aucun nom identique) |
| `src/core/logging.py` | — | — | Indépendant (aucun nom identique) |
| `src/core/types.py` | — | — | Indépendant (aucun nom identique) |
| `src/ui/__init__.py` | `core/__init__.py` | 0.00 % | Indépendant (fichier vide) |
| `src/ui/main_window.py` | `gui/main_window.py` | 12.33 % | **Inspiration** |

**Bloc partagé ≥ 3 lignes** (seul bloc trouvé) :

```text
old gui/main_window.py[34:37] / new src/ui/main_window.py[72:75]



class MainWindow(QMainWindow):
```

Il s'agit de la déclaration de classe et de son socle Qt, pas d'un corps de méthode copié. Les deux fichiers diffèrent ensuite par l'API (PyQt5 vs PySide6), les imports, les widgets et les méthodes.

Note : plusieurs `__init__.py` existent dans `12a505c` ; la comparaison a retenu `core/__init__.py` comme premier candidat. Les fichiers `src/*/__init__.py` actuels sont vides (0 octet), sauf `src/adapters/usb/__init__.py` (173 octets), d'où les taux très faibles.

## 3. `OperationError` / `OperationFailure` / `ChipsetType` / `DeviceInfo` dans `12a505c`

Commande : `git grep -n -E "OperationError|OperationFailure|ChipsetType|DeviceInfo" 12a505c -- "*.py"`

```text
12a505c:core/detector.py:30:    from core.usb_scanner import UsbScanner, UsbDeviceInfo, scan_mtk_devices, HAS_PYUSB
12a505c:core/detector.py:665:                # Conversion UsbDeviceInfo → ConnectedDevice (modèle unifié du détecteur)
12a505c:core/usb_scanner.py:165:class UsbDeviceInfo:
12a505c:core/usb_scanner.py:205:            f"UsbDeviceInfo(VID={self.vid:04X} PID={self.pid:04X} "
12a505c:core/usb_scanner.py:227:    Méthode principale : scan_mtk_devices() → List[UsbDeviceInfo]
12a505c:core/usb_scanner.py:228:    Méthode secondaire : scan_all_devices()  → List[UsbDeviceInfo]
12a505c:core/usb_scanner.py:260:    def _classify_usb_device(self, device) -> Optional[UsbDeviceInfo]:
12a505c:core/usb_scanner.py:262:        Classifie un périphérique USB brut (objet usb.core.Device) en UsbDeviceInfo.
12a505c:core/usb_scanner.py:296:        return UsbDeviceInfo(
12a505c:core/usb_scanner.py:311:    def scan_mtk_devices(self) -> List[UsbDeviceInfo]:
12a505c:core/usb_scanner.py:322:        Retourne : Liste de UsbDeviceInfo, triée par priorité BROM > NORMAL > USB_NORMAL.
12a505c:core/usb_scanner.py:327:        results: List[UsbDeviceInfo] = []
12a505c:core/usb_scanner.py:371:    def scan_all_devices(self) -> List[UsbDeviceInfo]:
12a505c:core/usb_scanner.py:374:        Retourne UsbDeviceInfo uniquement pour les VID MediaTek et Android reconnus.
12a505c:core/usb_scanner.py:379:        results: List[UsbDeviceInfo] = []
12a505c:core/usb_scanner.py:406:                results.append(UsbDeviceInfo(
12a505c:core/usb_scanner.py:457:def scan_mtk_devices() -> List[UsbDeviceInfo]:
12a505c:gui/__init__.py:6:from gui.device_info_tab import DeviceInfoTab
12a505c:gui/__init__.py:24:    "DeviceInfoTab",
12a505c:gui/device_info_tab.py:90:class DeviceInfoTab(QWidget):
```

Conclusion : **aucun** fichier `12a505c` ne contient `OperationError`, `OperationFailure` ou `ChipsetType`. Les seules occurrences de `DeviceInfo` sont des sous-chaînes de `UsbDeviceInfo` (`core/usb_scanner.py`, `core/detector.py`) et de `DeviceInfoTab` (`gui/__init__.py`, `gui/device_info_tab.py`). Les types du cœur actuels ne proviennent donc pas de `12a505c`.

## 4. Provenance de `bin/libusb-1.0.dll` et des autres binaires

| Binaire | Octets | SHA-256 | Référence officielle | Conclusion |
|---|---:|---|---|---|
| `bin/AdbWinApi.dll` | 108184 | `c1d653030b4bde65d3e07e4d0b0979e17be56df1436cdd15528630f27808050d` | non vérifié | Non traçable |
| `bin/AdbWinUsbApi.dll` | 73368 | `0710e894d9b40f71a670c13c694079d564c92c1279da382cfe4850983aaebe1b` | non vérifié | Non traçable |
| `bin/adb.exe` | 8273560 | `b4a6b455702684652cccf7b46258b29e653538904359a58fd4931cf3ef286b3f` | non vérifié (empreinte vue sur FileScan.io, verdict « Trusted » ; pas de confirmation Google) | Non traçable |
| `bin/fastboot.exe` | 2429080 | `b2d9cbff4ce9ae7eb448cfc831bafc867935f50f5be38f8f81057fd7eb3b8d86` | non vérifié | Non traçable |
| `bin/libusb-1.0.dll` | 166400 | `62ccefaf3f99dc46f6739f803391958cf77c8bc9cb5cf44acda8512709a404db` | non vérifié | Non traçable |
| `bin/x64/libusb-1.0.dll` | 166400 | `62ccefaf3f99dc46f6739f803391958cf77c8bc9cb5cf44acda8512709a404db` | non vérifié | Non traçable |
| `redist/VC_redist.x64.exe` | 25635768 | `cc0ff0eb1dc3f5188ae6300faef32bf5beeba4bdd6e8e445a9184072096b713b` | non vérifié | Non traçable |

Notes factuelles :
- `bin/libusb-1.0.dll` et `bin/x64/libusb-1.0.dll` ont la **même empreinte SHA-256** : ce sont deux copies identiques du même binaire.
- La recherche en ligne n'a trouvé aucune correspondance pour l'empreinte libusb. Pour `adb.exe`, l'empreinte apparaît sur FileScan.io avec un verdict « Trusted », mais ce n'est pas le site officiel Google ; la confirmation n'est donc pas faite.
- Les empreintes sont enregistrées ci-dessus pour une vérification ultérieure contre les releases officielles (platform-tools Google, libusb.info, Microsoft).

## 5. Modèle de licence antérieur

### 5.1 `git log --all --oneline -- "*license*" "*token*"`

```text
50afa9b feat: cœur, configuration, journalisation, adaptateurs et détection USB
fbc7c61 chore: repartir d'une base propre et ajouter les documents de cadrage
7f7822c refactor(license): hide tokens in UI and load activation tokens from external file
b883e8e fix(license): harden activation with absolute paths, error.log traceback, and crash-safe dialog
f8d3d0d feat: ajouter licence offline 14j, lecture infos ADB et widget compte à rebours
```

### 5.2 `git show 7f7822c --stat`

```text
commit 7f7822ca0f0957322e5ebca9bf721193289a48e8
Author: Optima MTK Dev <dev@optima-mtk.tools>
Date:   Sat Nov 7 00:12:11 2026 -0800

    refactor(license): hide tokens in UI and load activation tokens from external file

 core/license_manager.py | 92 +++++++++++++++++++++++++++++--------------------
 gui/license_dialog.py   | 32 +++++------------
 tokens.json             |  7 ++++
 3 files changed, 70 insertions(+), 61 deletions(-)
```

### 5.3 `git show 3379aeb --stat`

```text
commit 3379aebfbfaf65a3f9a3b496c679bef6d8c26646
Author: Optima MTK Dev <dev@optima-mtk.tools>
Date:   Sat Nov 7 00:44:50 2026 -0800

    fix(robustness): appliquer correctifs anti-crash C.1 à C.5 de l'audit licence

 core/detector.py   |  47 ++++++++++++++----------
 gui/main_window.py | 103 +++++++++++++++++++++++++++++++++----------------
 main.py            |  12 +++++--
 3 files changed, 102 insertions(+), 60 deletions(-)
```

### 5.4 Résumé factuel

Le système de licence antérieur a été ajouté **après** `12a505c`, dans les commits `f8d3d0d`, `b883e8e` et `7f7822c` (7 novembre 2026, auteur `Optima MTK Dev <dev@optima-mtk.tools>`). Il s'agissait d'un système **offline** : `core/license_manager.py` validait un token lu dans un fichier externe `tokens.json` ou `tokens.txt`, stockait la date d'activation et une expiration de 14 jours dans `license.json`, et journalisait les erreurs dans `error.log`. `gui/license_dialog.py` fournissait une boîte de dialogue PyQt5 d'activation. Le commit `7f7822c` a sorti les tokens de l'interface vers `tokens.json` (7 lignes ajoutées), et `3379aeb` a durci l'activation (chemins absolus, traceback dans `error.log`, dialogue anti-crash). Le gestionnaire n'importe que la bibliothèque standard (`json`, `os`, `sys`, `traceback`, `datetime`, `typing`) : **aucun** `cryptography`, `requests`, `urllib` ou `socket`. Les références à `socket` trouvées dans `audit_usb.py` et `main.py` concernent le port TCP 5037 d'ADB, pas la licence. Le `requirements.txt` de `12a505c` liste PyQt5, pyserial, pyusb et libusb-package ; aucun appel réseau lié à la licence n'a été trouvé.

## 6. Recommandations

**Scénario A — Aucune copie.** Aucune preuve de copie : la similarité maximale est de 12.33 % sur `main_window.py`, limitée à la déclaration `class MainWindow(QMainWindow):`. Continuer la phase 3 sans purge, en consignant ce rapport et en vérifiant les empreintes des binaires avant release.

**Scénario B — Inspiration structurelle.** `src/ui/main_window.py` partage le nom du module et de la classe avec `gui/main_window.py`, mais le code diffère (PySide6 vs PyQt5, méthodes et structure différentes). Documenter ce point dans un `PROVENANCE.md`, continuer la phase 3.

**Scénario C — Copie avérée.** Non applicable en l'état : aucun bloc de code métier copié n'a été trouvé (le seul bloc ≥ 3 lignes est la déclaration de classe). Si une copie était démontrée, il faudrait bloquer la phase 3, purger l'historique, réécrire les fichiers concernés et lancer un audit licence complet.

## Verdict

**PROVENANCE AMBIGUË — DOCUMENTER ET CONTINUER**