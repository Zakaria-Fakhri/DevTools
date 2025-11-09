from typing import Iterable, Iterator, Any, List

def stream_csv_lines(file_path: str) -> Iterator[str]:
    """Yield CSV lines from a file lazily.
    
    Parameters:
    file_path (str): Der Pfad zur CSV-Datei.
    
    Returns:
    Iterator[str]: Iterator von Zeilen aus der Datei.
    """
    
    # Öffne die Datei im Lesemodus mit UTF-8 Encoding
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        # Iteriere durch alle Zeilen
        for line in f:
            # Entferne Zeilenumbrüche am Ende und gib die Zeile zurück
            yield line.rstrip('\n\r')


def parse_csv_line(line: str, delimiter: str = ',') -> List[str]:
    """Parst eine CSV-Zeile in Felder.
    
    Parameters:
    line (str): Die zu parsende CSV-Zeile.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    List[str]: Liste der geparsten Felder.
    """
    
    # Liste für die geparsten Felder
    fields = []
    # Aktuelles Feld das aufgebaut wird
    f_cur = ''
    # Flag ob wir uns in Anführungszeichen befinden
    in_q = False
    # Index für die Iteration
    i = 0
    
    # Iteriere durch alle Zeichen in der Zeile
    while i < len(line):
        c = line[i]
        
        # Behandle Anführungszeichen
        if c == '"':
            if in_q:
                # Prüfe auf doppelte Anführungszeichen (escaped)
                if i + 1 < len(line) and line[i + 1] == '"':
                    f_cur += '"'
                    i += 1  # Überspringe das nächste Anführungszeichen
                else:
                    # Ende des quoteten Bereichs
                    in_q = False
            else:
                # Start des quoteten Bereichs
                in_q = True
        # Behandle Delimiter
        elif c == delimiter and not in_q:
            # Füge das aktuelle Feld zur Liste hinzu
            fields.append(f_cur)
            f_cur = ''
        else:
            # Normales Zeichen zum aktuellen Feld hinzufügen
            f_cur += c
        
        i += 1
    
    # Füge das letzte Feld hinzu
    fields.append(f_cur)
    
    return fields


def stream_csv_rows(file_path: str, delimiter: str = ',') -> Iterator[List[str]]:
    """Stream CSV rows from a file lazily.
    
    Parameters:
    file_path (str): Der Pfad zur CSV-Datei.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    Iterator[List[str]]: Iterator von geparsten Reihen.
    """
    
    # Iteriere durch alle Zeilen aus der Datei
    for line in stream_csv_lines(file_path):
        # Parse die Zeile und gib die Felder zurück
        yield parse_csv_line(line, delimiter)


def read_csv_with_headers(file_path: str, delimiter: str = ',') -> Iterator[dict]:
    """Liest CSV-Datei mit Headers als Dictionary-Stream.
    
    Parameters:
    file_path (str): Der Pfad zur CSV-Datei.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    Iterator[dict]: Iterator von Dictionaries (Header -> Wert).
    """
    
    # Hole den Stream von Reihen
    row_stream = stream_csv_rows(file_path, delimiter)
    
    # Erste Zeile sind die Headers
    headers = next(row_stream, None)
    
    # Wenn keine Headers vorhanden, beende
    if headers is None:
        return
    
    # Iteriere durch die restlichen Reihen
    for row in row_stream:
        # Erstelle ein Dictionary aus Headers und Werten
        row_dict = {}
        for i, h in enumerate(headers):
            # Füge Wert hinzu, oder None falls Index außerhalb
            row_dict[h] = row[i] if i < len(row) else None
        
        yield row_dict


def filter_csv_rows(file_path: str, 
                    filter_fn: Any, 
                    delimiter: str = ',') -> Iterator[List[str]]:
    """Filtert CSV-Zeilen basierend auf einer Funktion.
    
    Parameters:
    file_path (str): Der Pfad zur CSV-Datei.
    filter_fn: Funktion die eine Reihe nimmt und bool zurückgibt.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    Iterator[List[str]]: Iterator von gefilterten Reihen.
    """
    
    # Iteriere durch alle Reihen
    for row in stream_csv_rows(file_path, delimiter):
        # Prüfe ob die Reihe den Filter erfüllt
        if filter_fn(row):
            yield row


def count_csv_rows(file_path: str, delimiter: str = ',') -> int:
    """Zählt die Anzahl der Reihen in einer CSV-Datei.
    
    Parameters:
    file_path (str): Der Pfad zur CSV-Datei.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    int: Anzahl der Reihen (ohne Header).
    """
    
    # Zähler für Reihen
    cnt = 0
    
    # Iteriere durch alle Reihen
    for _ in stream_csv_rows(file_path, delimiter):
        cnt += 1
    
    return cnt
