init:
	python3 -m venv ./venv
	./venv/bin/pip install --upgrade pip

install:
	./venv/bin/pip install -r requirements.txt

run-dev:
	./venv/bin/python run.py

run-docker:
	cd ../ && docker-compose up --build backend