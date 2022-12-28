mypy:
	poetry run mypy src/ tests/

pytest:
	poetry run pytest --tb=short

flake8:
	poetry run flake8 src/ tests/
