from typing import Callable, Any


def retry_on_exception(func: Callable[..., Any], retries: int = 3, delay_seconds: float = 0.5) -> Callable[..., Any]:
	"""Wrapper um einen Aufruf bei Fehlern mehrfach zu wiederholen.

	Input: func (callable), retries (int), delay_seconds (float)
	Output: Callable, das das Ergebnis von func zurückgibt oder die Exception weiterreicht
	# to do: Implementiere den Wrapper, Sleep zwischen Versuchen und Logging der Fehler.
	"""
	raise NotImplementedError("# to do: retry_on_exception implementieren")

