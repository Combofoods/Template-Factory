pip:
	pip install -r requirements.txt

dev: pip	
	pip install -r requirements-dev.txt

build: dev
	@echo "Build the module"
	python setup.py sdist bdist_wheel
	pip install -e .
