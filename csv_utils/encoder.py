from typing import Iterable, Any

def encode_row(values: Iterable[Any], delimiter: str = ',') -> str:
    """Kodiert eine Reihe von Werten in eine CSV-Zeile.
    
    Parameters:
    values (Iterable[Any]): Die zu kodierenden Werte.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    str: Eine formatierte CSV-Zeile.
    """
    
    # Liste für die formatierten Werte
    v_enc = []
    
    # Iteriere durch alle Werte
    for v in values:
        # Behandle None-Werte als leere Strings
        if v is None:
            v_enc.append('')
        else:
            # Konvertiere den Wert zu einem String
            v_str = str(v)
            
            # Prüfe ob Escaping notwendig ist (Delimiter, Anführungszeichen oder Zeilenumbruch)
            if delimiter in v_str or '"' in v_str or '\n' in v_str or '\r' in v_str:
                # Escape Anführungszeichen durch Verdopplung
                v_str = v_str.replace('"', '""')
                # Umschließe den Wert mit Anführungszeichen
                v_str = f'"{v_str}"'
            
            v_enc.append(v_str)
    
    # Verbinde alle Werte mit dem Delimiter
    return delimiter.join(v_enc)


def encode_stream(rows: Iterable[Iterable[Any]], delimiter: str = ',') -> Iterable[str]:
    """Kodiert mehrere Reihen als Stream von CSV-Zeilen.
    
    Parameters:
    rows (Iterable[Iterable[Any]]): Die zu kodierenden Reihen.
    delimiter (str): Das Trennzeichen (Standard: ',').
    
    Returns:
    Iterable[str]: Ein Generator von CSV-Zeilen.
    """
    
    # Iteriere durch alle Reihen
    for r in rows:
        # Kodiere jede Reihe mit encode_row und gib sie zurück
        yield encode_row(r, delimiter)
