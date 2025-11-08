from typing import Dict, Any

def validate_json_schema(obj: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """Validiert ein JSON-Objekt gegen ein Schema.
    
    Parameters:
    obj (Dict[str, Any]): Das zu validierende Objekt.
    schema (Dict[str, Any]): Das Schema zur Validierung.
    
    Returns:
    bool: True wenn gültig, False sonst.
    
    Schema-Format:
    {
        "type": "object" | "string" | "number" | "integer" | "boolean" | "array" | "null",
        "required": ["field1", "field2"],  # Nur für type="object"
        "properties": {                     # Nur für type="object"
            "field1": {...},
            "field2": {...}
        },
        "items": {...}                      # Nur für type="array"
    }
    """
    
    # Hole den erwarteten Typ aus dem Schema
    s_type = schema.get("type", "object")
    
    # Validiere den Typ
    if s_type == "null":
        return obj is None
    elif s_type == "boolean":
        return isinstance(obj, bool)
    elif s_type == "integer":
        return isinstance(obj, int) and not isinstance(obj, bool)
    elif s_type == "number":
        return isinstance(obj, (int, float)) and not isinstance(obj, bool)
    elif s_type == "string":
        return isinstance(obj, str)
    elif s_type == "array":
        # Prüfe ob obj eine Liste ist
        if not isinstance(obj, list):
            return False
        # Validiere Array-Items wenn Schema vorhanden
        s_items = schema.get("items")
        if s_items:
            for item in obj:
                if not validate_json_schema(item, s_items):
                    return False
        return True
    elif s_type == "object":
        # Prüfe ob obj ein Dictionary ist
        if not isinstance(obj, dict):
            return False
        
        # Prüfe required Fields
        s_req = schema.get("required", [])
        for f_req in s_req:
            if f_req not in obj:
                return False
        
        # Validiere Properties wenn Schema vorhanden
        s_props = schema.get("properties", {})
        for f_name, f_val in obj.items():
            # Wenn Property im Schema definiert ist, validiere sie
            if f_name in s_props:
                if not validate_json_schema(f_val, s_props[f_name]):
                    return False
        
        return True
    else:
        # Unbekannter Typ
        return False
