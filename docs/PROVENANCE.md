# PROVENANCE

## Antériorité

Le projet v0.5 interne **OptimaMTKTool** (commit `12a505c`, PyQt5, non publié, même auteur) est antérieur à ce dépôt. Il n'est ni repris ni distribué ici.

## Réécriture

Le code actuel a été écrit sous **PySide6 (LGPL)** à partir de `docs/SPEC.md`, `docs/ARCHITECTURE.md`, `docs/STACK.md` et `docs/LEGAL.md`. Voir `docs/RAPPORT_TRANSPOSITION.md` : **similarité normalisée maximale 3,67 %, aucune séquence de 3 lignes identiques, aucune signature PyQt5 résiduelle**.

## Point MainWindow

La classe MainWindow porte le même nom que dans la v0.5 pour des raisons de convention Qt (nommage standard d'une fenêtre principale) ; aucun bloc de son corps n'est partagé.

## Inspiration licence

Le système de licence de la v0.5 (commits `f8d3d0d`, `b883e8e`, `7f7822c`) — offline 14 jours, fichier `tokens.json` externe, `license.json` avec expiration, aucun appel réseau — sera examiné en phase 2 pour inspirer la licence hybride Ed25519 + 72 h hors ligne. Aucun code n'est repris à ce stade.

## Dépendances tierces

`PySide6`/`shiboken6` (LGPL-3.0-only, ADR-002), `pyusb` (BSD), `PyYAML` (MIT). Aucune dépendance GPL dans le cœur.

## Binaires tiers

Aucun binaire n'est versionné dans optima-flash/. `libusb-1.0.dll` est fourni par le technicien via `scripts/install_drivers.ps1` (source : libusb.info).

## Signature

Je soussigné, digitalholding2026-ux, auteur du projet Optima Telecom Flash Tool, déclare que le code source de ce dépôt a été écrit indépendamment de la v0.5 mentionnée ci-dessus, sous réserve des éléments documentés dans docs/RAPPORT_TRANSPOSITION.md.