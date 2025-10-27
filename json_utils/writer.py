from typing import Any, Dict


def write_json(obj: Dict[str, Any], path: str, indent: int = 2) -> None:
	"""Schreibt ein Objekt als JSON in eine Datei.

	Input: obj (dict), path (str), indent (int)
	Output: None
	# to do: Öffne Datei sicher, schreibe JSON mit Encoding und sichere atomar, falls möglich.
	"""
	raise NotImplementedError("# to do: write_json implementieren")

