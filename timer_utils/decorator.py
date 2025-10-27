from typing import Callable, Any


def timed(func: Callable[..., Any]) -> Callable[..., Any]:
	"""Dekorator: Leitet Aufruf an Timer weiter und gibt das Ergebnis zurück.

	Input: func
	Output: dekorierte Funktion
	# to do: Implementiere Dekorator der Ausführungszeit misst und ggf. loggt.
	"""
	raise NotImplementedError("# to do: timed dekorator implementieren")

