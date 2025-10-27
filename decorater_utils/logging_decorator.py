from typing import Callable, Any


def log_calls(logger_name: str = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
	"""Dekorator: Loggt Ein-/Ausgabe und Exceptions einer Funktion.

	Input: optional logger_name
	Output: dekorator
	# to do: Implementiere Logging der Eingabeparameter, des Ergebnisses und Exceptions.
	"""
	raise NotImplementedError("# to do: log_calls dekorator implementieren")

