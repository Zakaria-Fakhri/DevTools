from typing import Callable, Any


def retry(retries: int = 3, delay: float = 0.5) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
	"""Dekorator: Wiederhole einen Funktionsaufruf bei Ausnahme.

	Input: retries, delay
	Output: dekorator
	# to do: Implementiere dekorator, der Exceptions abfängt und erneut aufruft; erhalte Signatur.
	"""
	raise NotImplementedError("# to do: retry dekorator implementieren")

