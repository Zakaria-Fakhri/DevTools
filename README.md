# DevTools Collection

Eine Sammlung von wiederverwendbaren Entwickler-Tools für Python-Projekte.  
Dieses Repo ist modular aufgebaut, sodass jedes Modul in einem eigenen Unterordner organisiert ist.  

Ziel ist es, die Entwicklung zu beschleunigen, wiederverwendbare Tools zu sammeln und anderen Entwicklern die Möglichkeit zu geben, aktiv mitzuarbeiten.

---

## 📦 Inhalt

| Modul | Funktion |
|-------|---------|
| `json_utils` | JSON-Dateien lesen, schreiben, validieren |
| `excel_utils` | Excel-Dateien lesen, schreiben, formatieren |
| `csv_utils` | CSV-Dateien lesen & schreiben |
| `yaml_utils` | YAML-Dateien lesen & schreiben |
| `api_utils` | HTTP Requests, Retry-Mechanismen, Rate-Limiting |
| `file_utils` | Dateimanagement, Backups, Duplicate Finder |
| `logger` | Logging Helper für Projekte |
| `config_utils` | `.env` Loader, Config Validator |
| `timer_utils` | Timer, Stopwatch, Laufzeitmessung |
| `decorator_utils` | Nützliche Decorators: Logging, Retry, Timer |
| `cli_utils` | Kommandozeilen-Utilities |

---

## 🚀 Offene Aufgaben (Open Issues / Help Wanted)

Wir freuen uns über Mitwirkung! Jeder kann Aufgaben übernehmen.  
Bitte ein Issue erstellen und mit `[Help Wanted]` kommentieren, wenn du daran arbeitest.

### **JSON Utils**
- [ ] `reader.py` → Streaming-Unterstützung für große JSON-Dateien  
- [ ] `writer.py` → Pretty-Print & Unicode-Support verbessern  
- [ ] `validator.py` → JSON-Schema-Validierung implementieren  
- [ ] Unit-Tests für alle Funktionen schreiben  

### **Excel Utils**
- [ ] `reader.py` → Unterstützung für mehrere Sheets gleichzeitig  
- [ ] `writer.py` → `.csv` Export implementieren  
- [ ] `formatter.py` → Automatische Zellformatierung & Styling  
- [ ] Unit-Tests  

### **CSV Utils**
- [ ] Encoding-Automatik erkennen (`utf-8`, `latin1`)  
- [ ] Large-File Handling (Streaming, Chunked-Processing)  
- [ ] Unit-Tests  

### **YAML Utils**
- [ ] Reader & Writer erweitern (unterstützt Kommentare beim Schreiben)  
- [ ] Schema-Validation für Config-Dateien  
- [ ] Unit-Tests  

### **API Utils**
- [ ] `requests.py` → Rate-Limiting & Timeout-Handling  
- [ ] `retry.py` → Exponentielles Backoff bei Fehlversuchen  
- [ ] OAuth2 Support (Token Refresh, Bearer Token)  
- [ ] Unit-Tests und Mock-Tests für API Calls  

### **File Utils**
- [ ] Duplicate File Finder optimieren (hash-basiert)  
- [ ] Backup-Manager: automatische Sicherung von Ordnern  
- [ ] File Watcher für Hot Reload  
- [ ] Unit-Tests  

### **Logger**
- [ ] Custom Logger mit Rotating File Handler  
- [ ] Logging-Levels: INFO, DEBUG, WARNING, ERROR  
- [ ] Unit-Tests  

### **Config Utils**
- [ ] `.env` Loader erweitern: Type-Parsing & Default Values  
- [ ] Config Validator für YAML/JSON/ENV  
- [ ] Unit-Tests  

### **Timer Utils**
- [ ] Stopwatch & Timer als Context-Manager  
- [ ] Decorator für Funktionslaufzeit-Messung  
- [ ] Unit-Tests  

### **Decorator Utils**
- [ ] Retry Decorator für Funktionen mit HTTP Calls  
- [ ] Logging Decorator für Debugging  
- [ ] Timer Decorator für Laufzeit-Statistiken  
- [ ] Unit-Tests  

### **CLI Utils**
- [ ] Argument Parsing Helper (`argparse` Wrapper)  
- [ ] Common Commands für JSON/Excel/CSV/Files  
- [ ] Beispiel-Skripte für CLI-Nutzung  
- [ ] Unit-Tests  

---

## 📥 Installation

```bash
git clone https://github.com/DEIN_USERNAME/DevTools.git
cd DevTools
pip install -e .
