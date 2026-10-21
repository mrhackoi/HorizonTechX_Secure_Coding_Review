# Horizon TechX — Secure Coding Review

## 1. Project Overview

**Project:** Python Secure Demo Application  
**Organization:** Horizon TechX  
**Review type:** Secure coding review and local functional security tests  
**Technology:** Python, Flask, SQLite  
**Environment:** Local Kali Linux lab  
**Scope:** Demo application only; no external systems tested.

## 2. Objectives

- Review SQL query handling.
- Review password storage and authentication.
- Validate user-controlled input.
- Review error handling and development configuration.
- Verify expected behavior with automated tests.

## 3. Security Controls Implemented

### SQL Injection Prevention
Database queries use parameterized SQL statements instead of concatenating user input into SQL commands.

### Password Storage
Passwords are hashed using Werkzeug's password-hashing functions. The application does not intentionally store plaintext passwords.

### Authentication Error Handling
Failed login attempts receive a generic error message to reduce username enumeration through response text.

### Input Validation
Username, password and search-query lengths are checked before processing. The Flask request body also has a configured size limit.

### Local Development Configuration
Debug mode is disabled, and the server binds to 127.0.0.1 so it listens on the local machine only.

## 4. Findings and Remediation

| ID | Area | Risk before remediation | Remediation |
|---|---|---|---|
| SCR-01 | SQL query construction | High if user input is concatenated into SQL | Parameterized queries |
| SCR-02 | Password storage | High if passwords are stored in plaintext | Password hashing |
| SCR-03 | Login errors | Medium if responses reveal account existence | Generic authentication error |
| SCR-04 | Input validation | Medium if input is not bounded | Length checks and request-size limit |
| SCR-05 | Development configuration | High if debug mode is exposed publicly | Debug disabled; localhost binding |

These are review scenarios and risks associated with the insecure patterns. They are not claims that every issue was observed in a deployed system. No production system was assessed.

## 5. Test Results

Six automated tests were executed using Python's unittest framework.

| Test | Expected result | Observed result |
|---|---|---|
| Health endpoint | HTTP 200 | PASS |
| Valid product search | HTTP 200 | PASS |
| Empty search query | HTTP 400 | PASS |
| Search query over 100 characters | HTTP 400 | PASS |
| Registration and valid login | HTTP 201 and HTTP 200 | PASS |
| Incorrect password | HTTP 401 | PASS |

**Summary: 6 tests passed.**

Command used:

`python -W default -m unittest discover -s tests -v`

The final test run completed successfully with no ResourceWarning shown in the provided output.

## 6. Limitations

- Testing was performed against a local demonstration application.
- This was not a full penetration test or an independent third-party security assessment.
- Rate limiting, account lockout, CSRF controls for browser-based sessions, production secret management, and deployment hardening would require additional design and testing before public deployment.
- Results apply only to the tested code and test cases.

## 7. Conclusion

The demonstration application uses parameterized SQL, password hashing, input validation, generic login errors, and safer local development settings. All six automated tests passed in the final reported run.

## 8. Evidence

Add screenshots of:
1. Application JSON response.
2. Health-check response.
3. Valid product-search response.
4. Empty-input rejection.
5. Successful registration.
6. Successful login.
7. Incorrect-password rejection.
8. Six passing automated tests.

## 9. Ethical Scope

All testing was limited to the locally controlled demonstration application. No unauthorized systems or real user accounts were tested.
