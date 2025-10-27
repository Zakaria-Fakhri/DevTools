from typing import Iterable, Iterator, Any


def stream_csv_lines(file_path: str) -> Iterator[str]:
	"""Yield CSV lines from a file lazily.

	Input: file_path
	Output: Iterator[str] of raw lines
	# to do: Öffne Datei mit korrekter Encoding/Errors, yield Zeilen ohne Laden der ganzen Datei.
	"""
	raise NotImplementedError("# to do: stream_csv_lines implementieren")


def parse_csv_line(line: str, delimiter: str = ',') -> Iterable[str]:
	"""Parst eine CSV-Zeile in Felder.

	Input: line (str), delimiter
	Output: Iterable[str] (Felder)
	# to do: Implementiere korrektes Parsing inkl. Quotes und Escaping.
	"""
	raise NotImplementedError("# to do: parse_csv_line implementieren")

