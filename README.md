# troi-lab project template

This is a template repository for troi-lab projects.

It includes:

- `.gitignore`: organized as inclusion-list i.e. by default, everything is excluded from git tracking and if users want resources tracked by git they need to intentionally add them to the `.gitignore`-file.
- `project.toml`: basic project metadata
- `.pre-commit-config.yaml`: some pre-commit hooks

## Development Setup

To install all required project dependencies and setup pre-commit hooks, clone this repo and run

```bash
python scripts/dev_setup.py
```

Some basic `uv` commands:

```bash
# Add packages to the `pyproject.toml` with
uv add {package}

# Remove packages from the `pyproject.toml` with
uv remove {package}

# Sync package dependencies with your local environment (aka. install dependencies defined in `pyproject.toml`) with
uv sync

# Upgrade all versions in your `pyproject.toml`
uv sync --upgrade

# Update the `uv.lock` file with
uv lock
```


To run linter, execute:

```bash
uv run ruff check
```

To run code-formatter, execute:

```bash
uv run ruff format --diff
```

## Git-CI hints

If a non-package project should use git-ci, `--source=<project-name>` might help enabling code-coverage:  
`uv run python -m coverage run  --source=<project-name> test_suite.py`


## Best practices and further resources

- Comes with pre-configured commit-hooks from [https://github.com/uker-troi-lab/commit_hooks.git](https://github.com/uker-troi-lab/commit_hooks.git), including commit message checking, automated changelog generation and version bumping
- This project template uses [uv](https://github.com/astral-sh/uv) for dependency-management and python-packaging (see [features](https://docs.astral.sh/uv/getting-started/features/))
- Regularly run code-linter and code-formatter ([ruff](https://docs.astral.sh/ruff/)). To exclude lines from the linter, add `# noqa` to the end of the line.
- Whenever possible, format your commit messages according to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) ([commitizen](https://commitizen-tools.github.io/commitizen/) can help you with that)
- Use [semantic versioning](https://semver.org/)
- [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) your commits when incrementing versions or creating a new release
- `CHANGELOG.md` is updated on every commit using pre-commit hooks
