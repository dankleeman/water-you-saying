format:
    uv run ruff check --fix
    uv run ruff format

check:
    uv run ruff check
    uv run ruff format --check

test:
    uv run coverage run -m pytest --cov=app
