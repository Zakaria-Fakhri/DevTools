from typing import List, Dict, Any


def build_parser() -> Any:
	"""Erstellt und konfiguriert den ArgumentParser für die CLI.

	Input: none
	Output: instanziierter ArgumentParser
	# to do: Definiere Argumente, Flags und Subcommands; Rückgabe des Parsers.
	"""
	raise NotImplementedError("# to do: build_parser implementieren")


def parse_args(argv: List[str]) -> Dict[str, Any]:
	"""Parst übergebene Argumente und gibt ein dict mit Werten zurück.

	Input: argv (List[str])
	Output: Dict mit geparsten Werten
	# to do: Verwende build_parser(), parse_args und konvertiere Ergebnis in dict.
	"""
	raise NotImplementedError("# to do: parse_args implementieren")

