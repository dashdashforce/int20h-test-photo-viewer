init:
	python3 -m venv ./venv
	./venv/bin/pip install --upgrade pip

install-dev:
	./venv/bin/pip install -r ./requirements/dev.txt

install-prod:
	./venv/bin/pip install -r ./requirements/prod.txt

run-dev:
	./venv/bin/python run.py

run-docker:
	cd ../ && docker-compose up --build backend