.PHONY: venv install 

PYTHON = python
DEPENDENCIES = requirements.txt

install: venv
	. .venv/bin/activate && \
	    pip install -r $(DEPENDENCIES)
venv:
	$(PYTHON) -m venv .venv


