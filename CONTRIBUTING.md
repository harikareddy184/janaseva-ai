# Contributing to JanaSeva AI

Thank you for helping improve JanaSeva AI! This repository welcomes contributions of all kinds.

## How to Contribute

1. Fork the repository.
2. Create a branch with a descriptive name.
3. Make your changes.
4. Run formatting, linting, and tests locally.
5. Open a merge request with a clear description.

## Local Workflow

- Install runtime dependencies: `pip install -r requirements.txt`
- Install developer dependencies: `pip install -r requirements-dev.txt`
- Run the app: `streamlit run app.py`
- Run tests: `pytest`
- Run format checks: `black --check .`
- Run lint checks: `ruff check .`
- Run type checks: `mypy --ignore-missing-imports app.py tests`

## Code Style

- Python formatting is managed with Black.
- Static analysis is managed with Ruff and MyPy.

## Notes

This repository also includes `CONTRIBUTION.md` for legacy compatibility. Please use `CONTRIBUTING.md` as the authoritative guide.
