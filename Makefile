PYTHON_PACKAGE_NAME = MaiTet

PYTHONVERSION ?= python3
PYTHON = env/bin/$(PYTHONVERSION)

env:
	$(PYTHONVERSION) -m venv env
	env/bin/pip install pip-tools
	$(PYTHON) -m pip install -r requirements/development.txt

.PHONY: requirements
requirement:
	find requirements/ -name '*.txt' -type f -delete
	env/bin/pip-compile -v -o requirements/development.txt requirements/development.in

.PHONY: clean
clean:
	find . -name "*.py[co]" -delete
	rm -r env

.PHONY: test
test: env
	env/bin/pytest .

.PHONY: check
check: env
	env/bin/flake8 .
