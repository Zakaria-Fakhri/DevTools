from typing import Any, Dict
import json

def write_json(obj: Dict[str, Any], path: str, indent: int = 2) -> None:
    """Schreibt ein Objekt als JSON in eine Datei.
    
    Parameters:
    obj (Dict[str, Any]): Das zu schreibende Dictionary-Objekt.
    path (str): Der Pfad zur Zieldatei.
    indent (int): Die Anzahl der Leerzeichen für die Einrückung (Standard: 2).
    
    Returns:
    None
    """
    
    # Öffne die Datei im Schreibmodus mit UTF-8 Encoding
    with open(path, 'w', encoding='utf-8') as f:
        # Schreibe das JSON-Objekt in die Datei
        json.dump(obj, f, indent=indent, ensure_ascii=False)
