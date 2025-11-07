
# DevTools Collection

Eine Sammlung wiederverwendbarer Entwickler‑Tools für Python‑Projekte. Das Repository ist modular aufgebaut — jedes Modul liegt in einem eigenen Unterordner und enthält fokussierte Helferfunktionen.

Ziel: Entwicklung beschleunigen, wiederverwendbare Utilities bereitstellen und Mitwirkung erleichtern.

---

## Inhalt (Module)

| Modul (Ordner) | Kurzbeschreibung |
|---|---|
| `json_utils` | JSON-Dateien lesen, schreiben, Streaming-Unterstützung für große Dateien |
| `excel_utils` | Excel (.xlsx) lesen/schreiben, Sheet-Handling und Exporthilfen |
| `csv_utils` | CSV lesen & schreiben, Encoding-Handling, Streaming für große Dateien |
| `yaml_utils` | YAML lesen & schreiben, Unterstützung für Konfigurationsdateien |
| `api_utils` | HTTP-Request-Wrapper, Retry-Logik, Rate‑Limiting und Timeout-Helfer |
| `file_utils` | Dateimanagement, Backup-Utilities, Duplikat‑Finder |
| `logger` | Projekt‑Logger, Hilfsfunktionen für Logging-Konfiguration |
| `config_utils` | `.env` Loader, Config-Parsing & Validatoren |
| `timer_utils` | Timer, Stopwatch, Laufzeit‑Messungen (auch als Context‑Manager) |
| `decorater_utils` | Nützliche Decorators (Retry, Logging, Timer) — Beachte: Ordnername ist `decorater_utils` |
| `cli_utils` | Helfer für Kommandozeilen‑Schnittstellen (argparse Wrapper, Common Commands) |

---

## ✅ Checkliste: Funktionen nach Modul

Die folgende Checkliste listet typische, erwartete Funktionen für jedes Modul als Ausgangspunkt. Bitte abhaken, wenn eine Funktion implementiert und mit Unit‑Tests versehen ist.

- json_utils
  - [x] read_json(path: str) -> dict / iterator (Streaming)
  - [ ] write_json(obj, path: str, pretty: bool = True, ensure_ascii: bool = False)
  - [ ] stream_json(path: str) -> generator
  - [ ] validate_json(instance, schema)
  - [ ] unit tests für Reader/Writer/Validator

- excel_utils
  - [ ] read_excel(path: str, sheet: Optional[str|int] = None) -> DataFrame / list
  - [ ] write_excel(data, path: str, sheet: str = "Sheet1")
  - [ ] read_multiple_sheets(path: str) -> dict[sheet_name, data]
  - [ ] export_sheet_to_csv(path: str, sheet: str, csv_path: str)
  - [ ] apply_formatting(path: str, rules: dict)
  - [ ] unit tests

- csv_utils
  - [ ] read_csv(path: str, encoding: Optional[str] = None) -> iterator / DataFrame
  - [ ] write_csv(data, path: str, encoding: str = "utf-8")
  - [ ] detect_encoding(path: str) -> str
  - [ ] stream_csv(path: str, chunk_size: int) -> generator
  - [ ] unit tests (inkl. large-file tests)

- yaml_utils
  - [ ] read_yaml(path: str) -> dict
  - [ ] write_yaml(obj, path: str, preserve_comments: bool = False)
  - [ ] validate_yaml(instance, schema)
  - [ ] support for aliase/anchors & comments beim Schreiben
  - [ ] unit tests

- api_utils
  - [ ] request(method, url, **kwargs) -> response (Wrapper)
  - [ ] session_manager() / get_session()
  - [ ] retry_decorator / retry_logic (exponentielles Backoff)
  - [ ] rate_limiter (per host / per endpoint)
  - [ ] oauth2_helper (token refresh)
  - [ ] timeout handling & mockable tests
  - [ ] unit tests mit Mock/Responses

- file_utils
  - [ ] list_files(path, recursive: bool = True) -> generator
  - [ ] compute_hash(path, algo: str = "sha256") -> str
  - [ ] find_duplicates(path) -> list[pairs]
  - [ ] backup_folder(src, dest, keep_n: int = 5)
  - [ ] watch_folder(path, callback)
  - [ ] unit tests

- logger
  - [ ] get_logger(name, level: str = "INFO")
  - [ ] configure_logging(console: bool = True, file: Optional[str] = None, rotate: bool = True)
  - [ ] log_to_file_with_rotation(path, max_bytes, backup_count)
  - [ ] logging_decorator(func)
  - [ ] unit tests (inkl. Logging-Ausgaben prüfen)

- config_utils
  - [ ] load_env(path: str = ".env") -> dict
  - [ ] parse_env_types(values: dict, schema: dict) -> dict
  - [ ] load_config(path: str) -> dict (support json/yaml)
  - [ ] validate_config(config, schema)
  - [ ] unit tests

- timer_utils
  - [ ] Timer context manager (start/stop, elapsed)
  - [ ] stopwatch helper
  - [ ] timeit_decorator(func)
  - [ ] cumulative timing/statistics collector
  - [ ] unit tests

- decorater_utils
  - [ ] retry_decorator(retries: int, backoff: float)
  - [ ] logging_decorator(verbosity: str)
  - [ ] timer_decorator
  - [ ] cache_decorator (optional)
  - [ ] unit tests

- cli_utils
  - [ ] build_arg_parser(common_args: list)
  - [ ] subcommand decorator / helper
  - [ ] commands for json/csv/excel basic operations
  - [ ] usage examples / sample entrypoints
  - [ ] unit tests / integration tests

---

## Offene Aufgaben / Prioritäten

- Priorität A (unbedingt): Unit‑Tests für kritische IO‑Funktionen (JSON/CSV/Excel/HTTP).
- Priorität B (wichtig): Robustheit bei großen Dateien (Streaming / Chunking).
- Priorität C (nice‑to‑have): OAuth2, Rate‑Limiting Policies, File Watcher, erweiterte Formatierung.

---

## Installation

Klonen und lokal als editable installieren:

```bash
git clone https://github.com/Zakaria-Fakhri/DevTools.git
cd DevTools
pip install -e .
```

---

## Mitwirken

- Fork → Branch → Pull Request mit kurzer Beschreibung.
- Für neue Funktionen: Beispiel‑Snippet in README oder Modul‑README hinzufügen.
- Unit‑Tests beilegen (pytest empfohlen).

---

## Lizenz

Siehe LICENSE im Repository.

```
MIT
