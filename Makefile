PYTHON=/usr/bin/python3
VENV_DIR=./venv
VENV_DIR_PYTHON=$(VENV_DIR)/bin/python

prepare:
	@test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	@echo "Environment setup complete. To activate, use 'source $(VENV_DIR)/bin/activate'"

dev:
	$(VENV_DIR_PYTHON) -m uvicorn docker_assets.api.api:app --reload

update-requirements:
	$(VENV_DIR_PYTHON) -m pip freeze > ./docker_assets/api/requirements.txt

clean:
	rm -rf $(VENV_DIR)
