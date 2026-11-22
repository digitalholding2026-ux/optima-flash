# Rapport — Guide d'initialisation

**Date** : 2026-11-22
**Objet** : guide agent, script de bootstrap, commit et push.

## 1. Sections du guide

| # | Section | Présente |
|---|---|---|
| 1 | Prérequis machine | Oui |
| 2 | Clone et installation | Oui |
| 3 | Backend USB (manuel) | Oui |
| 4 | Pilotes USB appareils | Oui |
| 5 | Vérification de l'environnement | Oui |
| 6 | Lecture du contexte projet | Oui |
| 7 | Règles de travail | Oui |
| 8 | État du projet et prochaine étape | Oui |

## 2. Test de cohérence mentale

Manques identifiés et corrigés :

1. `python` peut être le stub Microsoft Store → `bootstrap.ps1` utilise `py -3.11` en primaire, avec repli sur `python --version` et message d'échec explicite.
2. `Activate.ps1` peut être bloqué par la stratégie d'exécution → ajout de `Set-ExecutionPolicy -Scope Process Bypass` et de l'appel direct `.venv\Scripts\python.exe`.
3. `pip-licenses` ne s'invoque pas via `python -m` → utilisation du console script `pip-licenses.exe`.
4. `check_drivers()` peut retourner `False` pour MTK/QC sans appareil ou pilote → ajout du dépannage par clé (`libusb_backend`, `mtk_vcom`, `qualcomm_9008`).
5. `docs/CONTRAT_CLI_MTKCLIENT.md` n'existe pas encore → indication explicite dans la section 8.
6. `bootstrap.ps1` ne doit ni créer le venv, ni télécharger, ni installer → précisé dans la section 5.

Aucune étape manquante après correction.

## 3. Validation syntaxique

`Parser::ParseFile scripts/bootstrap.ps1` → `SYNTAX OK`.

## 4. Commit et push

- Commit : `docs: guide d'initialisation pour agent et script de bootstrap` (créé).
- Remote : aucun (`git remote -v` vide).
- Push : **en attente de configuration remote**.

```powershell
git remote add origin <url-du-depot-optima-flash>
git push -u origin master
```