# Rapport de vérification 2.10

**Date** : 2026-11-22
**Objet** : vérifications de preuve avant ouverture de la phase 3.
**Méthode** : commandes brutes, aucune correction, aucun fichier source modifié.

## 1. État git et provenance du commit 12a505c

### 1.1 `git log --oneline -15`

```text
c7f6e0c fix: backend libusb, bannière UI et hygiène des types
3318d5c docs: rapport de fin de phase 2
c122140 feat: interface PySide6 et diagnostic des pilotes USB
50afa9b feat: cœur, configuration, journalisation, adaptateurs et détection USB
dcda53a chore: poser le socle du dépôt (arborescence, pyproject, README)
fbc7c61 chore: repartir d'une base propre et ajouter les documents de cadrage
3379aeb fix(robustness): appliquer correctifs anti-crash C.1 à C.5 de l'audit licence
e904064 docs(audit): add comprehensive license crash audit report
7f7822c refactor(license): hide tokens in UI and load activation tokens from external file
b883e8e fix(license): harden activation with absolute paths, error.log traceback, and crash-safe dialog
b03f8d9 fix: corriger indentation update_connection_state dans tft_widgets.py
474fbb5 fix: ajouter --collect-all gui et --collect-all core au build PyInstaller pour inclure les packages
accbe90 fix: utiliser imports relatifs dans le package gui pour le build PyInstaller, ajouter dossier exe au sys.path
c82fca0 feat: épurer l'interface GUI et ajouter système d'aide contextuelle (infobulles + guide d'atelier dynamique)
ff98641 fix: add project root to sys.path for gui package imports
```

### 1.2 `git status`

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### 1.3 `git show --stat 12a505c`

```text
commit 12a505cc7052b6f23a83f0e1a8d5b4cf2fcd200e
Author: Your Name <you@example.com>
Date:   Sun Nov 1 16:33:01 2026 -0800

    v5

 .gitignore                                         |     1 +
 OptimaMTKTool.spec                                 |    46 +
 README.md                                          |   109 +
 __pycache__/audit_usb.cpython-315.pyc              |   Bin 0 -> 17214 bytes
 __pycache__/main.cpython-315.pyc                   |   Bin 0 -> 2315 bytes
 assets/.gitkeep                                    |     4 +
 assets/icon.ico                                    |   Bin 0 -> 5141 bytes
 audit_usb.py                                       |   310 +
 bin/AdbWinApi.dll                                  |   Bin 0 -> 108184 bytes
 bin/AdbWinUsbApi.dll                               |   Bin 0 -> 73368 bytes
 bin/README.md                                      |    43 +
 bin/adb.exe                                        |   Bin 0 -> 8273560 bytes
 bin/fastboot.exe                                   |   Bin 0 -> 2429080 bytes
 bin/libusb-1.0.dll                                 |   Bin 0 -> 166400 bytes
 bin/setup_platform_tools.ps1                       |    48 +
 bin/x64/libusb-1.0.dll                             |   Bin 0 -> 166400 bytes
 build.bat                                          |    87 +
 build/OptimaMTKTool/Analysis-00.toc                |  2409 +++
 build/OptimaMTKTool/COLLECT-00.toc                 |   476 +
 build/OptimaMTKTool/EXE-00.toc                     |    90 +
 build/OptimaMTKTool/OptimaMTKTool.exe              |   Bin 0 -> 4755936 bytes
 build/OptimaMTKTool/OptimaMTKTool.pkg              |   Bin 0 -> 4442080 bytes
 build/OptimaMTKTool/PKG-00.toc                     |    66 +
 build/OptimaMTKTool/PYZ-00.pyz                     |   Bin 0 -> 4408625 bytes
 build/OptimaMTKTool/PYZ-00.toc                     |  1381 ++
 build/OptimaMTKTool/base_library.zip               |   Bin 0 -> 1425082 bytes
 build/OptimaMTKTool/localpycs/pyimod01_archive.pyc |   Bin 0 -> 5051 bytes
 build/OptimaMTKTool/localpycs/pyimod02_importers.pyc |   Bin 0 -> 32425 bytes
 build/OptimaMTKTool/localpycs/pyimod03_ctypes.pyc  |   Bin 0 -> 6672 bytes
 build/OptimaMTKTool/localpycs/pyimod04_pywin32.pyc |   Bin 0 -> 1705 bytes
 build/OptimaMTKTool/localpycs/struct.pyc           |   Bin 0 -> 308 bytes
 build/OptimaMTKTool/warn-OptimaMTKTool.txt         |    47 +
 build/OptimaMTKTool/xref-OptimaMTKTool.html        | 19124 +++++++++++++++++++
 build_exe.py                                       |   120 +
 build_installer.bat                                |   105 +
 core/__init__.py                                   |    59 +
 core/__pycache__/__init__.cpython-315.pyc          |   Bin 0 -> 1365 bytes
 core/__pycache__/actions.cpython-315.pyc           |   Bin 0 -> 53778 bytes
 core/__pycache__/com_detector.cpython-315.pyc      |   Bin 0 -> 677 bytes
 core/__pycache__/detector.cpython-315.pyc          |   Bin 0 -> 61372 bytes
 core/__pycache__/device_models.cpython-315.pyc     |   Bin 0 -> 11241 bytes
 core/__pycache__/init_env.cpython-315.pyc          |   Bin 0 -> 20693 bytes
 core/__pycache__/mtk_communication.cpython-315.pyc |   Bin 0 -> 12201 bytes
 core/__pycache__/usb_reset.cpython-315.pyc         |   Bin 0 -> 18704 bytes
 core/__pycache__/usb_scanner.cpython-315.pyc       |   Bin 0 -> 21747 bytes
 core/actions.py                                    |   969 +
 core/brom/__init__.py                              |    24 +
 core/brom/__pycache__/__init__.cpython-315.pyc     |   Bin 0 -> 627 bytes
 core/brom/__pycache__/handshake.cpython-315.pyc    |   Bin 0 -> 6762 bytes
 core/brom/handshake.py                             |   112 +
 core/com_detector.py                               |    33 +
 core/detector.py                                   |  1232 ++
 core/device_models.py                              |   139 +
 core/init_env.py                                   |   358 +
 core/mtk_communication.py                          |   204 +
 core/usb_reset.py                                  |   443 +
 core/usb_scanner.py                                |   478 +
 data/auth/README.md                                |    11 +
 data/da/README.md                                  |    14 +
 dist/OptimaMTKTool/OptimaMTKTool.exe               |   Bin 0 -> 4755936 bytes
 .../_internal/PyQt5/Qt5/bin/MSVCP140.dll           |   Bin 0 -> 590112 bytes
 .../_internal/PyQt5/Qt5/bin/MSVCP140_1.dll         |   Bin 0 -> 31728 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Core.dll            |   Bin 0 -> 6023664 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5DBus.dll            |   Bin 0 -> 436720 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Gui.dll             |   Bin 0 -> 7008240 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Network.dll         |   Bin 0 -> 1340400 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Qml.dll             |   Bin 0 -> 3591664 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5QmlModels.dll       |   Bin 0 -> 438768 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Quick.dll           |   Bin 0 -> 4148720 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Svg.dll             |   Bin 0 -> 330736 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5WebSockets.dll      |   Bin 0 -> 149488 bytes
 .../_internal/PyQt5/Qt5/bin/Qt5Widgets.dll         |   Bin 0 -> 5498352 bytes
 .../_internal/PyQt5/Qt5/bin/VCRUNTIME140.dll       |   Bin 0 -> 101872 bytes
 .../_internal/PyQt5/Qt5/bin/VCRUNTIME140_1.dll     |   Bin 0 -> 44528 bytes
 .../_internal/PyQt5/Qt5/bin/d3dcompiler_47.dll     |   Bin 0 -> 4173928 bytes
 .../_internal/PyQt5/Qt5/bin/libEGL.dll             |   Bin 0 -> 25072 bytes
 .../_internal/PyQt5/Qt5/bin/libGLESv2.dll          |   Bin 0 -> 3385328 bytes
 .../_internal/PyQt5/Qt5/bin/opengl32sw.dll         |   Bin 0 -> 20923392 bytes
 .../PyQt5/Qt5/plugins/generic/qtuiotouchplugin.dll |   Bin 0 -> 68080 bytes
 .../PyQt5/Qt5/plugins/iconengines/qsvgicon.dll     |   Bin 0 -> 41968 bytes
 .../PyQt5/Qt5/plugins/imageformats/qgif.dll        |   Bin 0 -> 39408 bytes
 .../PyQt5/Qt5/plugins/imageformats/qicns.dll       |   Bin 0 -> 45040 bytes
 .../PyQt5/Qt5/plugins/imageformats/qico.dll        |   Bin 0 -> 38384 bytes
 .../PyQt5/Qt5/plugins/imageformats/qjpeg.dll       |   Bin 0 -> 421360 bytes
 .../PyQt5/Qt5/plugins/imageformats/qsvg.dll        |   Bin 0 -> 32240 bytes
 .../PyQt5/Qt5/plugins/imageformats/qtga.dll        |   Bin 0 -> 31728 bytes
 .../PyQt5/Qt5/plugins/imageformats/qtiff.dll       |   Bin 0 -> 390128 bytes
 .../PyQt5/Qt5/plugins/imageformats/qwbmp.dll       |   Bin 0 -> 30192 bytes
 .../PyQt5/Qt5/plugins/imageformats/qwebp.dll       |   Bin 0 -> 510448 bytes
 .../PyQt5/Qt5/plugins/platforms/qminimal.dll       |   Bin 0 -> 844784 bytes
 .../PyQt5/Qt5/plugins/platforms/qoffscreen.dll     |   Bin 0 -> 754672 bytes
 .../PyQt5/Qt5/plugins/platforms/qwebgl.dll         |   Bin 0 -> 482288 bytes
 .../PyQt5/Qt5/plugins/platforms/qwindows.dll       |   Bin 0 -> 1477104 bytes
 .../plugins/platformthemes/qxdgdesktopportal.dll   |   Bin 0 -> 68592 bytes
 .../Qt5/plugins/styles/qwindowsvistastyle.dll      |   Bin 0 -> 144368 bytes
 .../_internal/PyQt5/Qt5/translations/qt_ar.qm      |   Bin 0 -> 130 bytes
 .../_internal/PyQt5/Qt5/translations/qt_bg.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_ca.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_cs.qm      |   Bin 0 -> 157 bytes
 .../_internal/PyQt5/Qt5/translations/qt_da.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_de.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_en.qm      |     1 +
 .../_internal/PyQt5/Qt5/translations/qt_es.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_fa.qm      |   Bin 0 -> 293121 bytes
 .../_internal/PyQt5/Qt5/translations/qt_fi.qm      |   Bin 0 -> 117 bytes
 .../_internal/PyQt5/Qt5/translations/qt_fr.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_gd.qm      |   Bin 0 -> 70 bytes
 .../_internal/PyQt5/Qt5/translations/qt_gl.qm      |   Bin 0 -> 323590 bytes
 .../_internal/PyQt5/Qt5/translations/qt_he.qm      |   Bin 0 -> 83 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_ar.qm |   Bin 0 -> 8743 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_bg.qm |   Bin 0 -> 10599 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_ca.qm |   Bin 0 -> 7444 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_cs.qm |   Bin 0 -> 15297 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_da.qm |   Bin 0 -> 4795 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_de.qm |   Bin 0 -> 7570 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_en.qm |     1 +
 .../_internal/PyQt5/Qt5/translations/qt_help_es.qm |   Bin 0 -> 10704 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_fr.qm |   Bin 0 -> 10922 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_gl.qm |   Bin 0 -> 10891 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_hu.qm |   Bin 0 -> 10284 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_it.qm |   Bin 0 -> 10612 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_ja.qm |   Bin 0 -> 7917 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_ko.qm |   Bin 0 -> 5708 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_pl.qm |   Bin 0 -> 9673 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_ru.qm |   Bin 0 -> 7288 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_sk.qm |   Bin 0 -> 10388 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_sl.qm |   Bin 0 -> 10363 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_tr.qm |   Bin 0 -> 4629 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_uk.qm |   Bin 0 -> 9750 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_zh_CN.qm |   Bin 0 -> 6441 bytes
 .../_internal/PyQt5/Qt5/translations/qt_help_zh_TW.qm |   Bin 0 -> 9301 bytes
 .../_internal/PyQt5/Qt5/translations/qt_hu.qm      |   Bin 0 -> 146 bytes
 .../_internal/PyQt5/Qt5/translations/qt_it.qm      |   Bin 0 -> 153 bytes
 .../_internal/PyQt5/Qt5/translations/qt_ja.qm      |   Bin 0 -> 146 bytes
 .../_internal/PyQt5/Qt5/translations/qt_ko.qm      |   Bin 0 -> 146 bytes
 .../_internal/PyQt5/Qt5/translations/qt_lt.qm      |   Bin 0 -> 165383 bytes
 .../_internal/PyQt5/Qt5/translations/qt_lv.qm      |   Bin 0 -> 89 bytes
 .../_internal/PyQt5/Qt5/translations/qt_pl.qm      |   Bin 0 -> 161 bytes
 .../_internal/PyQt5/Qt5/translations/qt_pt.qm      |   Bin 0 -> 70334 bytes
 .../_internal/PyQt5/Qt5/translations/qt_ru.qm      |   Bin 0 -> 164 bytes
 .../_internal/PyQt5/Qt5/translations/qt_sk.qm      |   Bin 0 -> 157 bytes
 .../_internal/PyQt5/Qt5/translations/qt_sl.qm      |   Bin 0 -> 228428 bytes
 .../_internal/PyQt5/Qt5/translations/qt_sv.qm      |   Bin 0 -> 65851 bytes
 .../_internal/PyQt5/Qt5/translations/qt_tr.qm      |   Bin 0 -> 110 bytes
 .../_internal/PyQt5/Qt5/translations/qt_uk.qm      |   Bin 0 -> 164 bytes
 .../_internal/PyQt5/Qt5/translations/qt_zh_CN.qm   |   Bin 0 -> 117347 bytes
 .../_internal/PyQt5/Qt5/translations/qt_zh_TW.qm   |   Bin 0 -> 141 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_ar.qm  |   Bin 0 -> 160017 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_bg.qm  |   Bin 0 -> 165337 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_ca.qm  |   Bin 0 -> 210159 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_cs.qm  |   Bin 0 -> 174701 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_da.qm  |   Bin 0 -> 181387 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_de.qm  |   Bin 0 -> 220467 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_en.qm  |     1 +
 .../_internal/PyQt5/Qt5/translations/qtbase_es.qm  |   Bin 0 -> 165170 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_fi.qm  |   Bin 0 -> 179941 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_fr.qm  |   Bin 0 -> 166167 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_gd.qm  |   Bin 0 -> 189580 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_he.qm  |   Bin 0 -> 138690 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_hu.qm  |   Bin 0 -> 160494 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_it.qm  |   Bin 0 -> 161172 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_ja.qm  |   Bin 0 -> 129911 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_ko.qm  |   Bin 0 -> 156799 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_lv.qm  |   Bin 0 -> 153608 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_pl.qm  |   Bin 0 -> 162982 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_ru.qm  |   Bin 0 -> 203767 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_sk.qm  |   Bin 0 -> 125763 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_tr.qm  |   Bin 0 -> 194487 bytes
 .../_internal/PyQt5/Qt5/translations/qtbase_uk.qm  |   Bin 0 -> 158274 bytes
 .../PyQt5/Qt5/translations/qtbase_zh_TW.qm         |   Bin 0 -> 127849 bytes
 dist/OptimaMTKTool/_internal/PyQt5/QtCore.pyd      |   Bin 0 -> 2483712 bytes
 dist/OptimaMTKTool/_internal/PyQt5/QtGui.pyd       |   Bin 0 -> 2494976 bytes
 dist/OptimaMTKTool/_internal/PyQt5/QtWidgets.pyd   |   Bin 0 -> 5144576 bytes
 .../_internal/PyQt5/sip.cp315-win_amd64.pyd        |   Bin 0 -> 121856 bytes
 dist/OptimaMTKTool/_internal/VCRUNTIME140.dll      |   Bin 0 -> 178616 bytes
 dist/OptimaMTKTool/_internal/VCRUNTIME140_1.dll    |   Bin 0 -> 50112 bytes
 dist/OptimaMTKTool/_internal/_bz2.pyd              |   Bin 0 -> 86240 bytes
 dist/OptimaMTKTool/_internal/_ctypes.pyd           |   Bin 0 -> 144096 bytes
 dist/OptimaMTKTool/_internal/_decimal.pyd          |   Bin 0 -> 326368 bytes
 dist/OptimaMTKTool/_internal/_hashlib.pyd          |   Bin 0 -> 72928 bytes
 dist/OptimaMTKTool/_internal/_lzma.pyd             |   Bin 0 -> 171744 bytes
 dist/OptimaMTKTool/_internal/_multiprocessing.pyd  |   Bin 0 -> 38112 bytes
 dist/OptimaMTKTool/_internal/_queue.pyd            |   Bin 0 -> 36064 bytes
 dist/OptimaMTKTool/_internal/_socket.pyd           |   Bin 0 -> 88288 bytes
 dist/OptimaMTKTool/_internal/_ssl.pyd              |   Bin 0 -> 200416 bytes
 dist/OptimaMTKTool/_internal/_wmi.pyd              |   Bin 0 -> 39648 bytes
 dist/OptimaMTKTool/_internal/_zstd.pyd             |   Bin 0 -> 506592 bytes
 dist/OptimaMTKTool/_internal/assets/.gitkeep       |     4 +
 dist/OptimaMTKTool/_internal/assets/icon.ico       |   Bin 0 -> 5141 bytes
 dist/OptimaMTKTool/_internal/base_library.zip      |   Bin 0 -> 1425082 bytes
 dist/OptimaMTKTool/_internal/bin/AdbWinApi.dll     |   Bin 0 -> 108184 bytes
 dist/OptimaMTKTool/_internal/bin/AdbWinUsbApi.dll  |   Bin 0 -> 73368 bytes
 dist/OptimaMTKTool/_internal/bin/README.md         |    43 +
 dist/OptimaMTKTool/_internal/bin/adb.exe           |   Bin 0 -> 8273560 bytes
 dist/OptimaMTKTool/_internal/bin/fastboot.exe      |   Bin 0 -> 2429080 bytes
 dist/OptimaMTKTool/_internal/bin/libusb-1.0.dll    |   Bin 0 -> 166400 bytes
 .../_internal/bin/setup_platform_tools.ps1         |    48 +
 .../OptimaMTKTool/_internal/bin/x64/libusb-1.0.dll |   Bin 0 -> 166400 bytes
 dist/OptimaMTKTool/_internal/data/auth/README.md   |    11 +
 dist/OptimaMTKTool/_internal/data/da/README.md     |    14 +
 dist/OptimaMTKTool/_internal/drivers/README.md     |    41 +
 .../drivers/adb_fastboot/android_winusb.inf        |    56 +
 .../_internal/drivers/install_drivers.bat          |    27 +
 .../_internal/drivers/install_drivers.ps1          |    80 +
 .../drivers/libusb_filter/mtk_brom_filter.inf      |    44 +
 .../_internal/drivers/vcom/cdc-acm.inf             |    53 +
 dist/OptimaMTKTool/_internal/libcrypto-3.dll       |   Bin 0 -> 6021880 bytes
 dist/OptimaMTKTool/_internal/libffi-8.dll          |   Bin 0 -> 39696 bytes
 dist/OptimaMTKTool/_internal/libssl-3.dll          |   Bin 0 -> 1308920 bytes
 dist/OptimaMTKTool/_internal/libusb-1.0.dll        |   Bin 0 -> 166400 bytes
 dist/OptimaMTKTool/_internal/pyexpat.pyd           |   Bin 0 -> 215264 bytes
 dist/OptimaMTKTool/_internal/python3.dll           |   Bin 0 -> 76512 bytes
 dist/OptimaMTKTool/_internal/python315.dll         |   Bin 0 -> 7910624 bytes
 dist/OptimaMTKTool/_internal/select.pyd            |   Bin 0 -> 32992 bytes
 .../setuptools/_vendor/jaraco/text/Lorem ipsum.txt |     2 +
 dist/OptimaMTKTool/_internal/unicodedata.pyd       |   Bin 0 -> 753376 bytes
 dist/OptimaMTKTool/bin/AdbWinApi.dll               |   Bin 0 -> 108184 bytes
 dist/OptimaMTKTool/bin/AdbWinUsbApi.dll            |   Bin 0 -> 73368 bytes
 dist/OptimaMTKTool/bin/README.md                   |    43 +
 dist/OptimaMTKTool/bin/adb.exe                     |   Bin 0 -> 8273560 bytes
 dist/OptimaMTKTool/bin/fastboot.exe                |   Bin 0 -> 2429080 bytes
 dist/OptimaMTKTool/bin/libusb-1.0.dll              |   Bin 0 -> 166400 bytes
 dist/OptimaMTKTool/bin/setup_platform_tools.ps1    |    48 +
 dist/OptimaMTKTool/bin/x64/libusb-1.0.dll          |   Bin 0 -> 166400 bytes
 dist/OptimaMTKTool/data/auth/README.md             |    11 +
 dist/OptimaMTKTool/data/da/README.md               |    14 +
 dist/OptimaMTKTool/drivers/README.md               |    41 +
 .../drivers/adb_fastboot/android_winusb.inf        |    56 +
 dist/OptimaMTKTool/drivers/install_drivers.bat     |    27 +
 dist/OptimaMTKTool/drivers/install_drivers.ps1     |    80 +
 .../drivers/libusb_filter/mtk_brom_filter.inf      |    44 +
 .../drivers/vcom/cdc-acm.inf                       |    53 +
 dist/OptimaMTKTool/libusb-1.0.dll                  |   Bin 0 -> 166400 bytes
 drivers/README.md                                  |    41 +
 drivers/adb_fastboot/android_winusb.inf            |    56 +
 drivers/install_drivers.bat                        |    27 +
 drivers/install_drivers.ps1                        |    80 +
 drivers/libusb_filter/mtk_brom_filter.inf          |    44 +
 drivers/vcom/cdc-acm.inf                           |    53 +
 gui/__init__.py                                    |    31 +
 gui/__pycache__/__init__.cpython-315.pyc           |   Bin 0 -> 897 bytes
 .../connection_assistant.cpython-315.pyc           |   Bin 0 -> 19909 bytes
 gui/__pycache__/dashboard.cpython-315.pyc          |   Bin 0 -> 18689 bytes
 gui/__pycache__/device_info_tab.cpython-315.pyc    |   Bin 0 -> 21466 bytes
 .../device_status_widget.cpython-315.pyc           |   Bin 0 -> 11163 bytes
 gui/__pycache__/flash_tab.cpython-315.pyc          |   Bin 0 -> 13457 bytes
 gui/__pycache__/frp_tab.cpython-315.pyc            |   Bin 0 -> 24601 bytes
 gui/__pycache__/log_panel.cpython-315.pyc          |   Bin 0 -> 9275 bytes
 gui/__pycache__/main_window.cpython-315.pyc        |   Bin 0 -> 32640 bytes
 gui/__pycache__/tft_widgets.cpython-315.pyc        |   Bin 0 -> 57093 bytes
 gui/__pycache__/tools_tab.cpython-315.pyc          |   Bin 0 -> 33581 bytes
 gui/connection_assistant.py                        |   367 +
 gui/dashboard.py                                   |   328 +
 gui/device_info_tab.py                             |   352 +
 gui/device_status_widget.py                        |   171 +
 gui/flash_tab.py                                   |   259 +
 gui/frp_tab.py                                     |   429 +
 gui/log_panel.py                                   |   168 +
 gui/main_window.py                                 |   506 +
 gui/tft_widgets.py                                 |   836 +
 gui/tools_tab.py                                   |   539 +
 install.bat                                        |    55 +
 install_dependencies.ps1                           |    76 +
 installer.iss                                      |   263 +
 main.py                                            |   162 +
 path/to/filename.js                                |     2 +
 redist/VC_redist.x64.exe                           |   Bin 0 -> 25635768 bytes
 requirements.txt                                   |     4 +
 tools/AdbWinApi.dll                                |   Bin 0 -> 108184 bytes
 tools/AdbWinUsbApi.dll                             |   Bin 0 -> 73368 bytes
 tools/README.txt                                   |    20 +
 tools/adb.exe                                      |   Bin 0 -> 8273560 bytes
 tools/fastboot.exe                                 |   Bin 0 -> 2429080 bytes
 tools/libusb-1.0.dll                               |   Bin 0 -> 166400 bytes
 274 files changed, 34254 insertions(+)
```

### 1.4 `git show 12a505c -- bin/libusb-1.0.dll`

```text
commit 12a505cc7052b6f23a83f0e1a8d5b4cf2fcd200e
Author: Your Name <you@example.com>
Date:   Sun Nov 1 16:33:01 2026 -0800

    v5

diff --git a/bin/libusb-1.0.dll b/bin/libusb-1.0.dll
new file mode 100644
index 0000000..4b1198d
Binary files /dev/null and b/bin/libusb-1.0.dll differ
```

### 1.5 Explication factuelle

Le commit `12a505c` est le dernier commit du projet d'origine (« v5 »), créé le 1er novembre 2026 par l'identité générique « Your Name <you@example.com> ». Le dépôt n'était pas vide au départ : il contenait 274 fichiers, dont `bin/libusb-1.0.dll` ; le commit `fbc7c61` a supprimé l'arborescence de travail mais conservé l'historique, ce qui explique la présence du DLL dans `12a505c`. Les modifications 2.8 apparaissaient dans `git status` parce qu'elles avaient été produites au tour précédent sans commit ; les modifications 2.9 n'existaient pas encore à ce moment. Les deux lots ont ensuite été commités ensemble dans `c7f6e0c`, d'où le `git status` propre actuel.

### 1.6 Provenance du binaire

**Écart à traiter avant release** : `bin/libusb-1.0.dll` est un binaire de 166 400 octets committé par une identité générique, sans empreinte SHA-256 ni provenance (build officiel libusb, version, source) documentée dans le dépôt. Il n'est pas dans l'arbre courant (supprimé par le reset), mais reste accessible dans l'historique. Avant release, vérifier l'origine et l'empreinte du DLL, ou purger l'historique.

## 2. Preuve que `check_license()` est appelé dans l'UI

### 2.1 `grep -n "check_license" src/ui/main_window.py`

```text
34:from src.core.license import check_license
87:        self._license_ok = check_license()
```

### 2.2 Appel

`src/ui/main_window.py:87` :

```python
        self._license_ok = check_license()
```

### 2.3 Barre de statut

`src/ui/main_window.py:166` :

```python
            f"{self._status_message} · Licence : {license_text} · "
```

### 2.4 `grep -n "check_license\|Licence" tests/test_main_window.py`

```text
28:    assert "Licence : OK (placeholder)" in window._status_label.text()
```

Aucun test ne mocke ni n'affirme explicitement l'appel à `check_license()` ; le test ligne 28 vérifie seulement l'effet (chaîne de statut), qui dépend de la valeur retournée par `check_license()`.

## 3. Contenu réel de l'ADR-002

### 3.1 `Get-Content docs/ARCHITECTURE.md | Select-Object -Skip 55 -First 40`

```text
- L'interface CLI des moteurs devient un **contrat versionné** : toute rupture est testée.
- Les dépendances GPL sont isolées dans un paquet séparé, installable indépendamment.
- Une revue juridique annuelle et un audit SPDX complètent la décision.

## ADR-002 — Élection LGPL pour PySide6 et shiboken6

**Statut** : accepté · **Date** : 2026-11-22 · **Portée** : licence et distribution des dépendances graphiques.

**Contexte** : `PySide6` et `shiboken6` sont publiés sous tri-licence
`LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only`.

**Décision** : le projet élit explicitement **LGPL-3.0-only** pour ces deux
dépendances. Ce choix est opposable et documenté ; il ne change pas la licence
du produit, qui reste **propriétaire**.

**Conséquences** :
- Distribution en **onedir**, jamais **onefile** : les bibliothèques Qt
  (`Qt6Core.dll`, `Qt6Gui.dll`, `Qt6Widgets.dll`, `shiboken6*.pyd`…) restent
  remplaçables par l'utilisateur, conformément à `STACK.md` §2.
- Les DLL Qt sont livrées à côté de l'exécutable, jamais fusionnées dans un
  binaire unique.
- La notice LGPL et la procédure de remplacement des bibliothèques sont
  incluses dans la distribution.
- `pip-licenses --fail-on="GPL"` reste le contrôle de non-régression ; il doit
  sortir en 0.
- Toute évolution de PySide6 vers une licence non LGPL impose un nouvel ADR.

**Vérification** : `pip-licenses` affiche `LGPL-3.0-only OR GPL-2.0-only OR
GPL-3.0-only` pour PySide6, PySide6-Essentials, PySide6-Addons et shiboken6 ;
le projet retient LGPL-3.0-only.
```

### 3.2 `Get-Content docs/ARCHITECTURE.md | Measure-Object -Line`

```text
Lines Words Characters Property
----- ----- ---------- --------
   64
```

### 3.3 Couverture de l'ADR

| Point exigé | Couvert | Preuve |
|---|---|---|
| Les 3 licences alternatives | Oui | `LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only` |
| Élection LGPL-3.0-only | Oui | « le projet élit explicitement **LGPL-3.0-only** » |
| Distribution onedir, jamais onefile | Oui | « Distribution en **onedir**, jamais **onefile** » |
| DLL Qt remplaçables | Oui | « restent remplaçables par l'utilisateur » et « jamais fusionnées dans un binaire unique » |

## 4. Verdict

**POINT À CLARIFIER — provenance de `bin/libusb-1.0.dll` (commit `12a505c`, auteur générique, aucune empreinte ni origine documentée) à traiter avant release.**