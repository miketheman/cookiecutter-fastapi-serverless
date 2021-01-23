# {{ cookiecutter.project_name }}

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A [FastAPI] [serverless] service

Generated using [cookiecutter-fastapi-template](https://github.com/miketheman/cookiecutter-fastapi-template).


## Dependencies

We have a few sets of dependencies - development, deployment, and runtime.

### Runtime Dependencies

- Python 3.8
- [FastAPI]
- Python packages installed via `pipenv install`

### Deployment Dependencies

- serverelss command line tool
- serverless plugins from `package.json`

### Development Dependencies

- Runtime Dependencies (see above)
- Python packages installed via `pipenv install --dev`

[FastAPI]: https://fastapi.tiangolo.com/
[serverless]: https://www.serverless.com/open-source/


## Structure

The main entry point to the service is `api.py`.
Start there.
