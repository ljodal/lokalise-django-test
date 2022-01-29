all : black mypy isort flake8

.PHONY: black
black:
	black --check project bin/*

.PHONY: mypy
mypy:
	mypy project
	mypy bin/translations

.PHONY: isort
isort:
	isort --check-only project bin/*

.PHONY: flake8
flake8:
	flake8 project bin/*
