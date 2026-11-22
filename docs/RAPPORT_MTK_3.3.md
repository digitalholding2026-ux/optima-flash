# Rapport MTK — prompt 3.3 (installation isolée, detect, read_info)

## 1. Option retenue : A (venv dédié `.venv-mtk/`)

**Justification** : l'isolation est stricte — les dépendances GPL/lourdes de mtkclient (pyusb, capstone, keystone-engine, unicorn, PySide6) ne peuvent pas contaminer `.venv/` ni casser l'ADR-001. La reproductibilité est assurée par un clone épinglé au commit `5a863ee` (tag `v2.1.4.1`) dans `vendor/mtkclient/` (ignoré par git) et une commande d'invocation explicite dans la configuration. La distribution reste simple : un seul chemin relatif `binaries.mtkclient_cmd` à renseigner, sans submodule ni `pip install --target`.

Installations réalisées :

```
git clone --recursive https://github.com/bkerler/mtkclient.git vendor/mtkclient
git -C vendor/mtkclient checkout 5a863eece86fcaa97cb8325cf747e0aae3c307e4
→ HEAD is now at 5a863ee Fix issue with reading flash / boot1 / boot2 in gui
→ 5a863eece86fcaa97cb8325cf747e0aae3c307e4 2026-03-18 20:44:58 +0100
python -m venv .venv-mtk
.venv-mtk\Scripts\python.exe -m pip install -U pip
.venv-mtk\Scripts\python.exe -m pip install -r vendor\mtkclient\requirements.txt
.venv-mtk\Scripts\python.exe -m pip install vendor\mtkclient
→ Successfully installed mtkclient-2.1.4
```

## 2. Preuve d'installation — `mtk.exe --help`

```
usage: mtk [-h] [--vid VID] [--pid PID] [--serialport [SERIALPORT]]
           [--noreconnect] [--stock] [--uartloglevel UARTLOGLEVEL]
           [--loglevel LOGLEVEL] [--write_preloader_to_file] [--generatekeys]
           [--iot] [--socid] [--auth AUTH] [--cert CERT] [--debugmode]
           [--loader LOADER] [--preloader PRELOADER] [--ptype PTYPE]
           [--var1 VAR1] [--uart_addr UART_ADDR] [--da_addr DA_ADDR]
           [--brom_addr BROM_ADDR] [--mode MODE] [--wdt WDT] [--skipwdt]
           [--crash] [--appid APPID] [--sectorsize SECTORSIZE]
           [--gpt-num-part-entries GPT_NUM_PART_ENTRIES]
           [--gpt-part-entry-size GPT_PART_ENTRY_SIZE]
           [--gpt-part-entry-start-lba GPT_PART_ENTRY_START_LBA]
           [--parttype PARTTYPE] [--skip SKIP]
           command ...

MTK Flash/Exploit Client V2.1.4 (c) B.Kerler 2018-2026

positional arguments:
  command
    printgpt            Print GPT Table information
    gpt                 Save gpt table to given directory
    r                   Read flash to filename
    rl                  Read all partitions from flash to a directory
    rf                  Read whole flash to file
    rs                  Read sectors starting at start_sector to filename
    ro                  Read flash starting at offset to filename
    w                   Write partition from filename
    wf                  Write flash from filename
    wl                  Write partitions from directory path to flash
    wo                  Write flash starting at offset to filename
    e                   Erase partition
    es                  Erase partition with sector count
    ess                 Erase sector with sector count
    footer              Read crypto footer from flash
    fs                  Mount as FUSE filesystem
    reset               Send reset command
    meta                Enter meta mode
    meta2               Enter meta mode (wdt)
    dumpbrom            Try to dump the bootrom
    dumpsram            Try to dump the sram
    dumppreloader       Try to dump the preloader
```

(107 lignes au total ; la suite liste `gettargetconfig`, `devices`, puis les options de connexion.)

Appel équivalent testé : `.venv-mtk\Scripts\python.exe -m mtk --help`

```
C:\Users\Docker\Desktop\optima-flash\.venv-mtk\Scripts\python.exe: No module named mtk
```

`mtk.py` est empaqueté comme `mtkclient/mtk.py` ; c'est donc le script console `mtk.exe` qui est configuré (`binaries.mtkclient_cmd: [".venv-mtk/Scripts/mtk.exe"]`).

## 3. Échantillons réels : NON TESTÉ — pas d'appareil

```
detect() → src.core.types.OperationFailure: Le backend libusb-1.0.dll est introuvable. Lancez scripts/install_drivers.ps1. [USB_BACKEND_MISSING]
mtk printgpt → "Preloader - Status: Waiting for PreLoader VCOM, please reconnect mobile/iot device to brom mode" (timeout 15 s, aucun matériel)
```

Aucun `docs/samples/mtk_*_sample.txt` créé. Le parseur est donc basé sur les formats observés dans les sources épinglées : `mtkclient/Library/Partitions/__init__.py` (`tostring`, lignes `Offset/Length/Flags`) et `mtkclient/Library/mtk_preloader.py` (`HW code:`, `HW Ver:`, `SW Ver:`, `CPU:`).

## 4. Tests — `pytest -v tests/test_mtk_adapter.py`

```
tests/test_mtk_adapter.py::test_detect_keeps_only_mtk_devices PASSED     [ 16%]
tests/test_mtk_adapter.py::test_read_info_parses_partitions PASSED       [ 33%]
tests/test_mtk_adapter.py::test_read_info_parses_target_config PASSED    [ 50%]
tests/test_mtk_adapter.py::test_read_info_nonzero_returncode_is_not_an_exception PASSED [ 66%]
tests/test_mtk_adapter.py::test_read_info_missing_binary_raises_operation_failure PASSED [ 83%]
tests/test_mtk_adapter.py::test_hardware_read_info_returns_hw_code SKIPPED [100%]

======================== 5 passed, 1 skipped in 0.15s =========================
```

Suite complète : `48 passed, 1 skipped` — `ruff check src tests` : All checks passed — `mypy --strict src/adapters/mtk/ src/core/config.py src/core/runner.py` : Success, no issues found in 4 source files.

## 5. Modifications

`src/adapters/mtk/adapter.py` (MediaTekAdapter réel + stub conservé), `src/core/config.py` (clé `binaries.mtkclient_cmd`), `config.yaml.example`, `.gitignore` (`.venv-mtk/`, `vendor/`), `tests/test_mtk_adapter.py`. Aucun import de `mtkclient` / `subprocess` / `usb` dans l'adaptateur ; aucun appel réseau.

Note d'installation : `requirements.txt` de mtkclient liste `keystone` ; PyPI résout ce nom vers OpenStack Keystone (30.0.0), sans rapport avec l'assembleur. `keystone-engine` est bien installé et n'a pas d'impact sur `printgpt` / `gettargetconfig`.

MTK DETECT+READ_INFO OK — test matériel REPORTÉ