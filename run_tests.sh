#!/bin/bash

function uv_init {
    uv lock
    uv pip install -r pyproject.toml
}

function test_code {
    python -m coverage run -m unittest
    coverage report
}

function code_linter {
    ruff check --output-format concise
}

function code_formatter {
    ruff format --diff
}

printf "Running unittests\n\n"
cd ./tests
uv_init
test_code

printf "Running linter\n\n"
cd ..
code_linter

printf "Running formatter\n\n"
code_formatter
