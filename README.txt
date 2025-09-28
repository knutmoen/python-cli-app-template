# Python CLI App Template

A simple CLI framework in Python.
Created just to have a simple project ready for playing around with python code. Just do a checkout and start coding.
No GUI implemented and no container-related setup. Just a simple CLI application ready for running locally on your machine.

## Prerequisites
- Python 3.8+ recommended
- Git

## 1) Clone the repository
```bash
git clone https://github.com/knutmoen/python-cli-app-template.git
cd python-cli-app-template
```

## 2) Create & activate a virtual environment
```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows (Powershell):
.venv\Scripts\Activate.ps1
```

## 3) Install dependencies
```bash
pip install -r requirements.txt
```

⚠️ **Note:** Make sure to always install dependencies after pulling changes, since test and coverage tools like `pytest-cov` are required.

## 4) Run the app (without installing)
Use the module entry point:
```bash
python -m mycli.cli hello
python -m mycli.cli add 5 10
```

## 5) (Optional) Install as a CLI command
Editable install so changes reflect immediately:
```bash
pip install -e .
mycli hello
mycli add 5 10
```

## 6) Run tests
```bash
pytest -q
```

## 7) Run tests with coverage
```bash
pytest --cov --cov-report=term-missing
```

This will:
- Use `.coveragerc` automatically
- Show missing lines inline in the terminal
- Generate a `coverage.xml` file (for CI/Codecov)

## 8) Add a new command
1. Create a new file in `mycli/operations/`, e.g. `reverse.py`.
2. Implement a `run(args)` function:
   ```python
   # mycli/operations/reverse.py
   def run(args):
       text = " ".join(args) if args else ""
       print(text[::-1])
   ```
3. Execute it:
   ```bash
   python -m mycli.cli reverse "some text here"
   # or, if installed:
   mycli reverse "some text here"
   ```

## Project structure
```
mycli/
  __init__.py
  cli.py
  operations/
    __init__.py
    hello.py
    add.py
tests/
  __init__.py
  test_hello.py
requirements.txt
setup.py
pyproject.toml
README.md
.coveragerc
```

## Continuous Integration (GitHub Actions)

This project includes a basic GitHub Actions workflow to run tests and track coverage on every push and pull request.

File is found at `.github/workflows/tests.yml`

## Troubleshooting
- **ModuleNotFoundError (operations/mycli not found):** Ensure you run commands from the project root and that you use `python -m mycli.cli ...` or install with `pip install -e .`.
- **Permission issues on Windows when activating venv:** Use PowerShell and run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again.
