from typing import Optional


class Timer:
	"""Ein einfacher Timer zur Messung von Abschnitten.

	Input: optionaler Name
	Methods: start(), stop(), elapsed()
	Output: elapsed seconds als float
	# to do: Implementiere start/stop mit Zeitstempeln und Thread-Safety falls nötig.
	"""

	def __init__(self, name: Optional[str] = None):
		raise NotImplementedError("# to do: Timer.__init__ implementieren")

	def start(self) -> None:
		raise NotImplementedError("# to do: Timer.start implementieren")

	def stop(self) -> float:
		raise NotImplementedError("# to do: Timer.stop implementieren")

	def elapsed(self) -> float:
		raise NotImplementedError("# to do: Timer.elapsed implementieren")

