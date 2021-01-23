"""
Use the `pytest-cookies` extension to write tests for the template generator.
See: https://pypi.org/project/pytest-cookies/
"""
import pytest


def test_bake_project_default(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "fastapi_template"
    assert result.project.isdir()
    # The app package is created inside the generated project directory
    assert result.project.join("app").isdir()


def test_bake_project_with_custom_name(cookies):
    result = cookies.bake(extra_context={"project_name": "Hello World"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "hello_world"
    assert result.project.isdir()


def test_bake_project_with_invalid_name(cookies):
    result = cookies.bake(extra_context={"project_name": "Awesome Project!"})
    assert result.exit_code == -1


def test_baked_proejct_contains_default_unmodified_files(cookies):
    result = cookies.bake()
    assert result.exit_code == 0

    # Do this test once post-bake, instead of in a parametrize decorator,
    # as the project doesn't change based on the parameter
    FILENAMES = [
        ".editorconfig",
        ".env",
        ".gitignore",
        "main.py",
        "LICENSE",
        "Pipfile",
        "README.md",
        "package.json",
        "pyproject.toml",
        "serverless.yml",
        "setup.cfg",
    ]
    for filename in FILENAMES:
        assert result.project.join(filename).check(file=1)


@pytest.mark.parametrize(
    "license_name",
    [
        "MIT License",
        "ISC License",
        "Apache License 2.0",
    ],
)
def test_open_source_liencese(cookies, license_name):
    result = cookies.bake(extra_context={"open_source_license": license_name})

    license_file = result.project.join("LICENSE")
    license_lines = license_file.readlines(cr=False)

    assert license_name in license_lines


def test_not_open_source(cookies):
    result = cookies.bake(extra_context={"open_source_license": "Not open source"})

    assert result.project.join("LICENSE").check(file=0)


def test_readme(cookies):
    result = cookies.bake()

    readme_file = result.project.join("README.md")
    readme_lines = readme_file.readlines(cr=False)

    assert "# FastAPI Template" in readme_lines


def test_serverless(cookies):
    result = cookies.bake()

    file = result.project.join("serverless.yml")
    lines = file.readlines(cr=False)

    assert "service: FastAPI-Template" in lines
