# JanSeva AI

JanSeva AI is an AI-powered civic assistant that helps Indian citizens access government services, Aadhaar support, civic complaint management, and public service information through a simple conversational interface.

## Features

- Aadhaar and identity service guidance
- Ration card support
- Civic complaint assistance
- App and service recommendations
- Streamlit-based web interface

## Installation

```bash
pip install -r requirements.txt
```

## Environment

Create a `.env` file from `.env.example` and set your API key:

```bash
copy .env.example .env
```

Then update `.env` with your `GROQ_API_KEY`.

## Run

```bash
python init_db.py
streamlit run app.py
```

## Development

Install developer dependencies:

```bash
pip install -r requirements-dev.txt
```

Run formatting and analysis:

```bash
black --check .
ruff check .
mypy --ignore-missing-imports app.py tests
pytest
```

## Contributing

See `CONTRIBUTING.md` for contribution guidelines.
