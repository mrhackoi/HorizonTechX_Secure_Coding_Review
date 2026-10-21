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


## 📸 Task 3 — Screenshot Evidence

### Screenshot 1
![Screenshot 1](1.png)

### Screenshot 2
![Screenshot 2](2.png)

### Screenshot 3
![Screenshot 3](3.png)

### Screenshot 4
![Screenshot 4](4.png)

### Screenshot 5
![Screenshot 5](5.png)

### Screenshot 6
![Screenshot 6](6.png)

### Screenshot 7
![Screenshot 7](7.png)

### Screenshot 8
![Screenshot 8](8.png)

### Screenshot 9
![Screenshot 9](9.png)

### Screenshot 10
![Screenshot 10](10.png)

### Screenshot 11
![Screenshot 11](11.png)

### Screenshot 12
![Screenshot 12](12.png)

### Screenshot 13
![Screenshot 13](13.png)

### Screenshot 14
![Screenshot 14](14.png)

### Screenshot 15
![Screenshot 15](15.png)

### Screenshot 16
![Screenshot 16](16.png)

### Screenshot 17
![Screenshot 17](17.png)


## Disclaimer
Educational local demo only; not production-ready.
