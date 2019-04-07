setup:
	pip install -r requirements.txt

run:
	python run.py

test:
	RACK_ENV=test DATABASE_URL=sqlite:///tmp/movies_test.db PYTHONPATH=./ python -m unittest discover -s tests/ -v