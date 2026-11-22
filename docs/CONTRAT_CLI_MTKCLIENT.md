# Contrat CLI — mtkclient

**Statut** : contrat d'interface documentaire. Aucune exécution, aucune installation.
**Périmètre** : F1 (détection) et F2 (lecture) ; flash/FRP documentés pour les prompts 3/4.

## 1. Version épinglée et provenance

| Élément | Valeur | Source |
|---|---|---|
| Dépôt officiel | `https://github.com/bkerler/mtkclient` | [S1] |
| Dernière release stable | `v2.1.4.1` (« Version 2.1.4 ») | [S2] |
| Commit du tag | `5a863eece86fcaa97cb8325cf747e0aae3c307e4` | [S3] |
| Date de publication | `2026-03-18T19:26:19Z` | [S2] |
| Licence | GPLv3 | [S4] |
| Branche par défaut | `main` (pas `master`) | [S2] ; `/commits/master` → 422 |
| PyPI | NON DISPONIBLE — `/pypi/mtkclient/json` et `/simple/mtkclient/` → 404 | [S5] |
| Installation officielle | `git clone --recursive` + `pip3 install -r requirements.txt` + `pip install .` | [S6] |
| Dépendances | wheel, setuptools, pyusb, pycryptodome, pycryptodomex, colorama, shiboken6, pyside6, pyserial, flake8, keystone-engine, capstone, unicorn, mfusepy | [S7] |

**Choix retenu** : clone git épinglé au tag `v2.1.4.1` / commit `5a863ee...`. Justification : PyPI n'expose pas le paquet (404), l'installation officielle passe par le dépôt, et les dépendances lourdes (capstone, keystone-engine, unicorn, pyusb, pyserial) rendent le build non trivial. **Ne pas installer dans le venv à cette étape.**

Sources :
- [S1] https://github.com/bkerler/mtkclient
- [S2] https://api.github.com/repos/bkerler/mtkclient/releases/latest
- [S3] https://api.github.com/repos/bkerler/mtkclient/tags
- [S4] https://raw.githubusercontent.com/bkerler/mtkclient/main/LICENSE
- [S5] https://pypi.org/pypi/mtkclient/json ; https://pypi.org/simple/mtkclient/
- [S6] https://raw.githubusercontent.com/bkerler/mtkclient/main/README-INSTALL.md
- [S7] https://raw.githubusercontent.com/bkerler/mtkclient/main/requirements.txt
- [S8] https://raw.githubusercontent.com/bkerler/mtkclient/main/README-USAGE.md
- [S9] https://raw.githubusercontent.com/bkerler/mtkclient/main/mtk.py

## 2. Commandes CLI utiles (documentation, pas exécution)

| Opération | Commande CLI exacte | Sortie attendue | Codes retour | Source |
|---|---|---|---|---|
| Détection preloader/BROM | `python mtk.py --preloader <preloader.bin>` (BROM) ; `python mtk.py --loader <DA>` (preloader) ; `python mtk.py --stock` (stock) ; `python mtk.py devices` (liste supportée) | texte (`%(levelname)s: %(message)s`) ; pas de JSON | NON DOCUMENTÉ | [S8], [S9] |
| Lecture infos | `python mtk.py printgpt` (GPT/partitions) ; `python mtk.py gettargetconfig` (target config) ; `python mtk.py logs` (logs) | texte | NON DOCUMENTÉ | [S8], [S9] |
| Flash partition | `python mtk.py w <partition> <filename>` | texte | NON DOCUMENTÉ | [S8] |
| Effacement FRP | `python mtk.py e <partition>` (générique) ; `frp` non nommé → **À CLARIFIER** | texte | NON DOCUMENTÉ | [S8], [S9] |

**Mode JSON** : NON — aucun `--json` / `--output-format` dans `mtk.py` ; le format de log est texte (`"%(levelname)s: %(message)s"`). Le parsing devra se faire sur stdout texte.

**Mode** : le mode BROM/preloader doit être fourni via `--preloader` ou `--loader` (ou `--stock`) ; sans cela, la cible n'est pas déterminée.

**Timeouts** : NON DOCUMENTÉ pour les 4 opérations.

**Codes retour** : NON DOCUMENTÉ.

## 3. Mapping DeviceInfo ↔ sortie mtkclient ↔ OperationResult

| DeviceInfo | Source mtkclient | Disponibilité | Dérivation |
|---|---|---|---|
| `chipset` | Implicite (MTK uniquement) | Disponible | `ChipsetType.MTK` |
| `connection_mode` | Args `--preloader` / `--loader` / `--stock`, logs | À dériver | PRELOADER si BROM/preloader ; UNKNOWN sinon |
| `vid` | Args `--vid`, logs de détection | À dériver | parsing stdout |
| `pid` | Args `--pid`, logs de détection | À dériver | parsing stdout |
| `bus` | — | Non disponible | mtkclient utilise un port série |
| `address` | — | Non disponible | idem |
| `serial` | Logs de détection | À dériver | parsing stdout ; sinon `None` |
| `model` | `gettargetconfig` (hw code) | À clarifier | le nom marketing n'est pas documenté |
| `partitions` | `printgpt` | Disponible | parsing du tableau GPT |
| `firmware_version` | `gettargetconfig`, logs | À clarifier | NON DOCUMENTÉ |

| OperationResult | Source | Disponibilité | Dérivation |
|---|---|---|---|
| `status` | exit code + logs | À dériver | SUCCESS si exit 0 et pas d'erreur ; FAILED sinon |
| `message` | stdout/stderr | Disponible | texte brut |
| `error` | logs | À dériver | parsing « Error: ... » ; sinon `OperationError` générique |
| `details` | stdout/stderr + artefacts | Disponible | texte brut, chemins de fichiers |

**À CLARIFIER** : 1) nom de la partition FRP et commande exacte ; 2) récupération du modèle/version firmware.

**CONTRAT PARTIEL — 2 À CLARIFIER**