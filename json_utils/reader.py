from typing import Any, Dict
import json

def read_json(path: str) -> Dict[str, Any]:
	"""Liest eine JSON-Datei und gibt das Objekt zurück.
	Input: path (str)
	Output: dict (geparstes JSON)
	# to do: Datei öffnen, JSON parsen, Fehler behandeln (FileNotFound, JSONDecodeError).
	"""
	try:
		# Datei öffnen
		with open(path, 'r', encoding='utf-8') as file:
			# JSON parsen
			data = json.load(file)
			return data
	except FileNotFoundError:
		# Fehlerbehandlung: Datei nicht gefunden
		raise FileNotFoundError(f"Die Datei '{path}' wurde nicht gefunden.")
	except json.JSONDecodeError:
		# Fehlerbehandlung: Ungültiges JSON
		raise json.JSONDecodeError(f"Die Datei '{path}' enthält kein gültiges JSON.", "", 0)
