PYTHON      := python3
ENV_ROOT    := $(shell pwd)/.env
ENV_BIN     := $(ENV_ROOT)/bin
PIP         := $(ENV_BIN)/pip
ISORT       := $(ENV_BIN)/isort
BLACK       := $(ENV_BIN)/black
FLAKE8      := $(ENV_BIN)/flake8
PYTEST      := $(ENV_BIN)/pytest

.PHONY: test

setup-venv:
	@rm -rf $(ENV_ROOT)
	@$(PYTHON) -m venv $(ENV_ROOT)
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requirements.txt

upgrade-deps:
	@$(PIP) install --upgrade pip isort black flake8 pytest

save-deps:
	@$(PIP) freeze > requirements.txt

format:
	@echo "Running isort"
	@$(ISORT) *.py
	@echo "Running black"
	@$(BLACK) *.py

check-format:
	@echo "Running isort"
	@$(ISORT) --check *.py
	@echo "Running black"
	@$(BLACK) --check *.py

lint:
	@echo "Running flake8"
	@$(FLAKE8) *.py

test:
	@echo "Running pytest"
	@$(PYTEST) -v
