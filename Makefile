PYTHON_PACKAGE_NAME = MaiTet

PYTHONVERSION ?= python3
PYTHON = env/bin/$(PYTHONVERSION)

.PHONY: init
init: requirements/development.in
	$(PYTHONVERSION) -m venv env
	env/bin/pip install pip-tools

.PHONY: requirements
requirement:
	find requirements/ -name '*.txt' -type f -delete
	env/bin/pip-compile -v -o requirements/development.txt requirements/development.in

.PHONY: env
env: requirements/development.txt
	$(PYTHON) -m pip install -r $<

.PHONY: clean
clean:
	find . -name "*.py[co]" -delete
	rm -r env

.PHONY: test
test: env
	pytest tests/

.PHONY: check
check: env
	env/bin/flake8 .
