"""Chargement de la configuration applicative.

Le fichier est cherché dans cet ordre : `config.yaml`, puis
`config.yaml.example`, puis valeurs par défaut. Les chemins relatifs sont
résolus à partir du dossier du fichier de configuration. Aucun secret n'est lu
ni stocké.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import yaml

__all__ = [
    "DEFAULT_CONFIG_FILENAME",
    "EXAMPLE_CONFIG_FILENAME",
    "AppConfig",
    "ConfigError",
    "load_config",
]

DEFAULT_CONFIG_FILENAME = "config.yaml"
EXAMPLE_CONFIG_FILENAME = "config.yaml.example"

DEFAULT_MTKCLIENT_PATH = "bin/mtkclient"
DEFAULT_EDL_PATH = "bin/edl"
DEFAULT_LOGS_DIR = "logs"
DEFAULT_RAW_DIR = "logs/raw"
DEFAULT_DB_PATH = "data/optima.db"
DEFAULT_THEME = "dark"
DEFAULT_MTKCLIENT_CMD: tuple[str, ...] = ()


class ConfigError(Exception):
    """Erreur de configuration (YAML malformé, type invalide, dossier inaccessible)."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


@dataclass(frozen=True, slots=True)
class AppConfig:
    """Configuration effective, avec chemins résolus."""

    mtkclient_path: Path
    edl_path: Path
    logs_dir: Path
    raw_dir: Path
    db_path: Path
    theme: str
    mtkclient_cmd: tuple[str, ...] = DEFAULT_MTKCLIENT_CMD


def _locate_config(path: Path | None) -> Path | None:
    if path is not None:
        candidate = path.expanduser()
        if not candidate.is_file():
            raise ConfigError(f"Fichier de configuration introuvable : {candidate}")
        return candidate

    for name in (DEFAULT_CONFIG_FILENAME, EXAMPLE_CONFIG_FILENAME):
        candidate = Path(name)
        if candidate.is_file():
            return candidate
    return None


def _read_yaml(path: Path) -> Mapping[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigError(f"Lecture impossible : {path}") from exc

    try:
        raw = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ConfigError(f"YAML malformé : {path}") from exc

    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ConfigError(f"Configuration invalide : {path} doit contenir un objet YAML.")
    return cast(dict[str, Any], raw)


def _section(data: Mapping[str, Any], key: str) -> Mapping[str, Any]:
    value = data.get(key)
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ConfigError(f"Configuration invalide : la section '{key}' doit être un dictionnaire.")
    return cast(Mapping[str, Any], value)


def _string(section: Mapping[str, Any], key: str, default: str) -> str:
    value = section.get(key, default)
    if not isinstance(value, str):
        raise ConfigError(f"Configuration invalide : '{key}' doit être une chaîne.")
    text = value.strip()
    if not text:
        raise ConfigError(f"Configuration invalide : '{key}' ne peut pas être vide.")
    return text


def _resolve(base_dir: Path, value: str) -> Path:
    candidate = Path(value).expanduser()
    return candidate if candidate.is_absolute() else base_dir / candidate


def _string_list(section: Mapping[str, Any], key: str) -> tuple[str, ...]:
    value = section.get(key)
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ConfigError(f"Configuration invalide : '{key}' doit être une liste de chaînes.")
    items: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ConfigError(
                f"Configuration invalide : '{key}' ne peut contenir que des chaînes non vides."
            )
        items.append(item.strip())
    return tuple(items)


def _resolve_cmd(base_dir: Path, cmd: tuple[str, ...]) -> tuple[str, ...]:
    """Résout le premier élément s'il ressemble à un chemin, laisse le reste intact."""
    if not cmd:
        return ()
    first = Path(cmd[0]).expanduser()
    if first.is_absolute() or len(first.parts) > 1:
        return (str(_resolve(base_dir, cmd[0])), *cmd[1:])
    return cmd


def _ensure_directories(config: AppConfig) -> None:
    for directory in (config.logs_dir, config.raw_dir, config.db_path.parent):
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            raise ConfigError(f"Création du dossier impossible : {directory}") from exc


def load_config(path: Path | None = None) -> AppConfig:
    """Charge la configuration et crée les dossiers configurés manquants."""
    config_path = _locate_config(path)

    data: Mapping[str, Any]
    if config_path is not None:
        data = _read_yaml(config_path)
        base_dir = config_path.resolve().parent
    else:
        data = {}
        base_dir = Path.cwd().resolve()

    binaries = _section(data, "binaries")
    paths = _section(data, "paths")
    ui = _section(data, "ui")

    config = AppConfig(
        mtkclient_path=_resolve(
            base_dir, _string(binaries, "mtkclient_path", DEFAULT_MTKCLIENT_PATH)
        ),
        edl_path=_resolve(base_dir, _string(binaries, "edl_path", DEFAULT_EDL_PATH)),
        logs_dir=_resolve(base_dir, _string(paths, "logs_dir", DEFAULT_LOGS_DIR)),
        raw_dir=_resolve(base_dir, _string(paths, "raw_dir", DEFAULT_RAW_DIR)),
        db_path=_resolve(base_dir, _string(paths, "db_path", DEFAULT_DB_PATH)),
        theme=_string(ui, "theme", DEFAULT_THEME),
        mtkclient_cmd=_resolve_cmd(base_dir, _string_list(binaries, "mtkclient_cmd")),
    )

    _ensure_directories(config)
    return config