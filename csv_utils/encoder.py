from typing import Iterable, Any


def encode_row(values: Iterable[Any], delimiter: str = ',') -> str:
	"""Kodiert eine Reihe von Werten in eine CSV-Zeile.

	Input: Iterable von Werten, optionaler Delimiter
	Output: eine formatierte CSV-Zeile als str
	# to do: Escaping, Typkonvertierung, None-Handling implementieren.
	"""
	raise NotImplementedError("# to do: encode_row implementieren")


def encode_stream(rows: Iterable[Iterable[Any]], delimiter: str = ',') -> Iterable[str]:
	"""Kodiert mehrere Reihen als Stream von CSV-Zeilen.

	Input: Iterable von Reihen (Iterable von Werten), Delimiter
	Output: Iterable von CSV-Zeilen (str)
	# to do: Verwende encode_row und yield jede Zeile; berücksichtige Performance.
	"""
	raise NotImplementedError("# to do: encode_stream implementieren")

