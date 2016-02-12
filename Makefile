install:
	pip install -r requirements.txt

test: install
	nosetests

watch: install
	nosetests --with-watch
