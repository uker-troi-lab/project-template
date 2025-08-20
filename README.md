# troi-lab project template

This is a template repository for troi-lab projects.

It includes:

- `.gitignore`: organized as inclusion-list i.e. by default, everything is excluded from git tracking and if users want resources tracked by git they need to intentionally add them to the `.gitignore`-file.
- `project.toml`: basic project metadata, including [commitizen](https://commitizen-tools.github.io/commitizen/) rules for formatting the `CHANGELOG.md`.
- `_templates/CHANGELOG.md.j2`: `CHANGELOG.md` template file. 

## Setup

To get started, run:

```bash
pip install uv commitizen
```

To generate a CHANGELOG.md, execute:

```bash
# make sure, you have previously installed `pip install commitizen`
cz ch --template _templates/CHANGELOG.md.j2 
```

## Best practices and further resources

- Whenever possible, format your commit messages according to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) ([commitizen](https://commitizen-tools.github.io/commitizen/) can help you with that)
- Use [semantic versioning](https://semver.org/)
- [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) your commits when incrementing versions or creating a new release
- Regularly update your `CHANGELOG.md`: `cz ch --template _templates/CHANGELOG.md.j2`
- This project template uses [uv](https://github.com/astral-sh/uv) for dependency-management and python-packaging (see [features](https://docs.astral.sh/uv/getting-started/features/))
