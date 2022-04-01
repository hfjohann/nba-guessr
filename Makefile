install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,E1120 cli.py &&\
		pylint --disable=R,C mlib.py &&\
		pylint --disable=R,C,W0613 test_cli.py

format:
	black *.py

test:
	python -m pytest -vv --cov=cli --cov==mlib test_cli.py

all: install lint format test
