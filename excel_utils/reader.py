from typing import List, Any


def read_excel(path: str, sheet: str = None) -> List[List[Any]]:
	"""Liest ein Excel-Sheet und gibt es als Liste von Reihen zurück.

	Input: path, optional sheet name/index
	Output: Liste von Reihen (jede Reihe: Liste von Zellen)
	# to do: Implementiere Lesen via openpyxl/xlrd, handle missing sheet, types.
	"""
	raise NotImplementedError("# to do: read_excel implementieren")

