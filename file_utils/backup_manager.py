from typing import List


def find_files_to_backup(root_path: str, patterns: List[str]) -> List[str]:
	"""Ermittelt Dateien, die gesichert werden sollen.

	Input: root_path, List von Glob-Patterns
	Output: Liste von Dateipfaden
	# to do: Implementiere Walk, Pattern-Matching und Filterung.
	"""
	raise NotImplementedError("# to do: find_files_to_backup implementieren")


def create_backup(paths: List[str], dest_folder: str) -> str:
	"""Erstellt ein Backup-Archiv (z.B. zip) aus gegebenen Pfaden.

	Input: Liste von Dateipfaden, Zielordner
	Output: Pfad zur erstellten Backup-Datei
	# to do: Implementiere Archiv-Erstellung, Fehlerbehandlung und Rückgabe des Pfads.
	"""
	raise NotImplementedError("# to do: create_backup implementieren")

