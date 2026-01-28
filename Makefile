install:
    pip install -e .

test:
    pytest

lint:
    ruff check .

format:
    ruff format .

build:
    python -m build