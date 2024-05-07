PYTHON=/usr/bin/python3
VENV_DIR=./venv
VENV_DIR_PYTHON=$(VENV_DIR)/bin/python

prepare:
	test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR_PYTHON) -m pip install -r ./docker_assets/producer/requirements.txt
	@echo "Environment setup complete. To activate, use 'source $(VENV_DIR)/bin/activate'"

dev:
	$(VENV_DIR_PYTHON) ./docker_assets/producer/producer.py

update-requirements:
	$(VENV_DIR_PYTHON) -m pip freeze > ./docker_assets/producer/requirements.txt

clean:
	rm -rf $(VENV_DIR)

start-source-infra:
	docker-compose up
	
stop-source-infra:
	docker compose down 

recreate-source-infra:
	docker compose down
	docker compose up --build

