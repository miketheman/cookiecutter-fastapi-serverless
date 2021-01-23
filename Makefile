.DEFAULT_GOAL := help

.PHONY: bake
bake:  ## Bake the cookiecutter template with default inputs
	@cookiecutter --no-input --overwrite-if-exists .

.PHONY: clean
clean: clean-pyc ## Remove all generated artifacts
	@rm -fr fastapi_template

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type f -name "*.py[co]" -delete
	@rm -fr .pytest_cache
	@find . -name '*~' -delete


.PHONY: setup
setup:  ## Set up project for development
	@pipenv install --dev

.PHONY: test
test:  ## Run test suite
	@pipenv run pytest --black $(ARGS) tests/

.PHONY: help
help:  ## Show this help (default)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
