# Rapport de vérification — backend USB (prompt 3.4 préalable)

## 1. Installation manuelle

Source : release officielle libusb **v1.0.30** (`https://github.com/libusb/libusb/releases/download/v1.0.30/libusb-1.0.30.7z`, issue depuis <https://libusb.info/>).

```
asset officiel : libusb-1.0.30.7z — 7484182 octets
extraction   : VS2019/MS64/dll/libusb-1.0.dll (x64)
copie 1      : .venv\Scripts\libusb-1.0.dll
copie 2      : .venv-mtk\Scripts\libusb-1.0.dll
```

Empreintes (identiques pour les deux copies) :

```
SHA-256       : E0CB1D0E8C20AE55C4E2F944D3136A2766EDE61A16551CC7562EAEDAE4BC13BC
Taille        : 165888 octets
FileVersion   : 1.0.30.12037
ProductVersion: 1.0.30.12037
Description   : C library for writing portable USB drivers in userspace
```

Note d'extraction : l'archive a été ouverte avec `py7zr` (aucun 7-Zip sur la machine). L'extraction s'est terminée par `UnsupportedCompressionMethodError` sur une entrée (méthode de compression non gérée par py7zr), mais `VS2019/MS64/dll/libusb-1.0.dll` a bien été extrait et se charge correctement (`ctypes.WinDLL` sur le chemin absolu).

## 2. Pourquoi un `sitecustomize.py` dans chaque venv

`ctypes.util.find_library` (utilisé par pyusb via `usb.libloader`) ne parcourt que `PATH` :

```
def find_library(name):
    for directory in os.environ['PATH'].split(os.pathsep):
        fname = os.path.join(directory, name)
        if os.path.isfile(fname):
            return fname
```

Recopiée à côté de `python.exe`, la DLL n'est donc pas trouvée par un `import usb.core` brut. Les deux venvs reçoivent un shim local (hors dépôt, dossiers ignorés par git) :

```
.venv\Lib\site-packages\sitecustomize.py
.venv-mtk\Lib\site-packages\sitecustomize.py
  → os.add_dll_directory(<venv>\Scripts) + <venv>\Scripts ajouté au PATH
```

À noter : mtkclient embarque sa propre `libusb-1.0.dll` (1.0.24.11584, SHA-256 6B24B0EE…) dans `mtkclient/Windows` et l'ajoute lui-même au PATH (`usblib.load_windows_dll`). La copie 1.0.30 dans `.venv-mtk\Scripts` sert donc aux usages pyusb directs du venv ; les opérations mtkclient utilisent la DLL embarquée.

## 3. Vérifications (sorties brutes)

```
=== 1 ===
True

=== 2 ===
[]

=== 3 ===
[<DEVICE ID 46f4:0001 on Bus 001 Address 001>, <DEVICE ID 1b36:000d on Bus 001 Address 000>, <DEVICE ID 0627:0001 on Bus 001 Address 002>]

=== 4 (Optima, brut) ===
[<DEVICE ID 46f4:0001 on Bus 001 Address 001>, <DEVICE ID 1b36:000d on Bus 001 Address 000>, <DEVICE ID 0627:0001 on Bus 001 Address 002>]
```

Commandes exactes :

```
.\.venv\Scripts\python.exe -c "from src.adapters.usb.drivers import check_backend; print(check_backend())"        → True
.\.venv\Scripts\python.exe -c "from src.adapters.usb.detector import detect_devices; print(detect_devices())"    → []
.\.venv-mtk\Scripts\python.exe -c "import usb.core; print(list(usb.core.find(find_all=True)))"                   → 3 périphériques, aucun NoBackendError
```

Écart constaté : la commande 3 ne renvoie pas `[]` mais la liste des périphériques USB de la machine (3 périphériques virtuels QEMU, aucun `VID_0E8D` MediaTek ni `VID_05C6&PID_9008` Qualcomm). `detect_devices()` reste bien `[]`. `usb.core.find(find_all=True)` renvoie par ailleurs un générateur ; `list(...)` a été utilisé pour obtenir une sortie lisible.

## 4. .gitignore et git status

`.gitignore` ne contenait aucune règle `*.dll` : ajout de `*.dll`, `*.exe`, `*.pyd`. Vérification :

```
git check-ignore -v .venv/Scripts/libusb-1.0.dll .venv-mtk/Scripts/libusb-1.0.dll
.gitignore:11:.venv/	.venv/Scripts/libusb-1.0.dll
.gitignore:12:.venv-mtk/	.venv-mtk/Scripts/libusb-1.0.dll

git status --porcelain
 M .gitignore
 M config.yaml.example
 M docs/CONTRAT_CLI_MTKCLIENT.md
 M docs/GUIDE_INITIALISATION.md
 M src/adapters/mtk/adapter.py
 M src/core/config.py
?? docs/RAPPORT_MTK_3.3.md
?? docs/RAPPORT_VERIF_RUNNER.md
?? src/core/runner.py
?? tests/test_mtk_adapter.py
?? tests/test_runner.py
```

Les seules modifications de ce prompt sont `.gitignore`, `docs/GUIDE_INITIALISATION.md` (§3 : deux copies + note `.venv-mtk`) et le présent rapport. Les autres entrées proviennent des prompts 3.2/3.3. Aucun fichier de `src/` n'a été touché.

BACKEND OK — PRÊT POUR 3.4