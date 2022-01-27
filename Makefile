all : black mypy isort flake8

.PHONY: black
black:
	black --check project

.PHONY: mypy
mypy:
	mypy project

.PHONY: isort
isort:
	isort --check-only project

.PHONY: flake8
flake8:
	flake8 project
