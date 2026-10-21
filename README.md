# HorizonTechX Secure Coding Review

Educational Flask application demonstrating secure coding practices.

## Technology
- Python
- Flask
- SQLite
- Werkzeug
- unittest

## Security Controls
- Parameterized SQL queries
- Password hashing
- Input validation
- Generic authentication errors
- Request size limit
- Debug mode disabled
- Localhost-only binding

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000/

## Run Tests
```bash
python -W default -m unittest discover -s tests -v
```

See SECURITY_AUDIT_REPORT.md for findings, fixes, tests and limitations.

## Disclaimer
Educational local demo only; not production-ready.
