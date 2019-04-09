setup:
	pip install -r requirements.txt

run:
	python run.py

setup.test:
	RACK_ENV=test DATABASE_URL=sqlite:///$(HOME)/movies_test.db flask db upgrade

test:
	RACK_ENV=test DATABASE_URL=sqlite:///$(HOME)/movies_test.db PYTHONPATH=./ python -W ignore::DeprecationWarning -m unittest discover -v -s tests/ -p '*_tests.py'

deploy:
	zappa deploy

themoviedb.crawler:
	python themoviedb_integration.py