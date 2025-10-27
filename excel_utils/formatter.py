from typing import Any, List


def format_cell(value: Any) -> str:
	"""Formatiert eine einzelne Zelle für Excel-Ausgabe.

	Input: beliebiger Wert
	Output: formatierter String
	# to do: Implementiere Datums-, Zahlen- und String-Formatierung.
	"""
	raise NotImplementedError("# to do: format_cell implementieren")


def format_rows(rows: List[List[Any]]) -> List[List[str]]:
	"""Formatiert mehrere Reihen (ruft format_cell auf).

	Input: rows als nested lists
	Output: gleiches Shape mit formatierten Strings
	# to do: Mappe format_cell über alle Zellen; beachte None und Sondertypen.
	"""
	raise NotImplementedError("# to do: format_rows implementieren")

