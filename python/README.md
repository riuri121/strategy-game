# Python Development

Core game logic and utilities written in Python.

## Setup

1. Create virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`

## Running

```bash
python main.py
```

## Testing

```bash
pytest
```

## Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## Structure

- `main.py` - Entry point
- `requirements.txt` - Dependencies
