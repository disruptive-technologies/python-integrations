PYTHON?=python3
PIP?=pip3
VENV?=venv

SHELL := /bin/bash

.PHONY: docs build venv VENV

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: setup.py
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV) || $(PYTHON) -m virtualenv --clear $(VENV)
	${VENV}/bin/python -m pip install --upgrade pip
	${VENV}/bin/python -m pip install -e .[dev]

build: venv
	${VENV}/bin/python setup.py sdist bdist_wheel

test: venv
	source ${VENV}/bin/activate && pytest tests/

coverage: venv
	source ${VENV}/bin/activate && pytest --cov=dtintegrations tests/

lint: venv
	source ${VENV}/bin/activate && mypy dtintegrations/ && flake8 dtintegrations/

clean:
	rm -rf build/ dist/ pip-wheel-metadata/ *.egg-info .pytest_cache/ .mypy_cache/ $(VENV) coverage.xml