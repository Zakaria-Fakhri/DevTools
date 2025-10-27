from typing import Any, Dict, Optional, Tuple


def send_request(method: str, url: str, headers: Optional[Dict[str, str]] = None, data: Any = None) -> Tuple[int, Any]:
	"""Sende eine HTTP-Anfrage.

	Input: method ("GET", "POST", ...), url (str), optional headers, optional data (payload)
	Output: Tuple(status_code:int, response_parsed:Any)
	# to do: Implementiere die eigentliche HTTP-Anfrage, Fehlerbehandlung und Parsen der Antwort.
	"""
	raise NotImplementedError("# to do: send_request implementieren")


def build_headers(token: Optional[str] = None) -> Dict[str, str]:
	"""Baue Standard-Header für Requests.

	Input: optional token (Bearer)
	Output: headers dict
	# to do: Füge Content-Type, Accept und ggf. Authorization hinzu.
	"""
	raise NotImplementedError("# to do: build_headers implementieren")

