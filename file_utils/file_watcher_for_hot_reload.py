from typing import Callable


def watch_directory(path: str, on_change: Callable[[str], None]) -> None:
	"""Beobachtet ein Verzeichnis und ruft callback bei Änderungen auf.

	Input: path, on_change callback (pfad->None)
	Output: None
	# to do: Implementiere Cross-Platform-Filewatching (watchdog oder Polling) und ruft on_change auf.
	"""
	raise NotImplementedError("# to do: watch_directory implementieren")

