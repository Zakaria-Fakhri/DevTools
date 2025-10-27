from typing import Dict, Any, Optional


def load_env_from_file(path: str) -> Dict[str, str]:
	"""Lädt Environment-Variablen aus einer Datei (z.B. .env oder YAML).

	Input: path (Dateipfad)
	Output: dict der key->value Umgebungsvariablen
	# to do: Datei lesen, Parsen (key=value oder YAML), Rückgabe eines Dicts.
	"""
	raise NotImplementedError("# to do: load_env_from_file implementieren")


def apply_env(env: Dict[str, str], overwrite: bool = False) -> None:
	"""Setzt die gegebenen Umgebungsvariablen in os.environ.

	Input: env dict, overwrite flag
	Output: None
	# to do: Setze Variablen in os.environ, respektiere overwrite.
	"""
	raise NotImplementedError("# to do: apply_env implementieren")

