PYTHON_PACKAGE_NAME = MaiTet

VIRTUALENV ?= env
PYTHONVERSION ?= python3
PYTHON = $(VIRTUALENV)/bin/$(PYTHONVERSION)

.PHONY: init
init: requirements/development.in
	find requirements/ -name '*.txt' -type f -delete
	$(PYTHONVERSION) -m venv $(VIRTUALENV)
	. "$(VIRTUALENV)/bin/activate"
	$(VIRTUALENV)/bin/pip install pip-tools
	$(VIRTUALENV)/bin/pip-compile -v -o requirements/development.txt requirements/development.in

$(VIRTUALENV): requirements/development.txt
	$(PYTHON) -m pip install -r $<

.PHONY: clean
clean:
	find . -name "*.py[co]" -delete
	rm -r $(VIRTUALENV)

.PHONY: test
test: $(VIRTUALENV)
	pytest tests/
