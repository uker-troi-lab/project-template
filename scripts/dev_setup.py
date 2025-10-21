# this files ensures to setup the expected development-repo-structure
# please adjust also ./src/{project_name}/__init__.py accordingly to
# make sure the dependencies on relative paths are added to the PATH
# environment variable.
# PLEASE MAKE SURE TO ADJUST REPOS (in setup_git_repos) AND
# (UN-) COMMENT THE REQUIRED SETUP-FUNCTIONS AT THE END OF THIS SCRIPT

import os
import logging
import subprocess

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

_project_root = os.path.abspath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
)


def create_conda_env(envname: str, pyversion: str = "3.12"):
    LOG.info(f"\nCreating conda-environment '{envname}'")
    _cmd = f"conda create -n {envname} python={pyversion}"
    subprocess.run(args=_cmd, shell=True)

    LOG.info("\nInstalling dependencies from 'pyproject.toml'")
    _install_cmd = (
        f"source activate {envname} && "
        "pip install uv && "
        "uv pip install -r pyproject.toml --all-extras"
    )
    subprocess.run(args=_install_cmd, shell=True, executable="/bin/bash")


def setup_git_repos(_project_root: str):
    logging.basicConfig(level=logging.INFO)
    url_dict = {
        "repo1": "https://url-to-git-host.com/repo1.git",
        "repo2": "https://url-to-git-host.com/repo2.git",
    }
    _setup_root = os.path.abspath(os.path.join(_project_root, "../"))
    LOG.info(f"setup_root: {_setup_root}")

    for _reponame, _repourl in url_dict.items():
        git_path = os.path.join(_setup_root, _reponame)
        if not os.path.isdir(git_path):
            LOG.warning(f"'{_reponame}' does not exist - downloading it.")
            _cmd = "git clone " + _repourl + " " + git_path
            subprocess.run(args=_cmd, shell=True)
        else:
            # pull latest version
            LOG.info(f"'{_reponame}' already exists - pulling latest version.")
            _cmd = "cd " + git_path + " && git pull"
            subprocess.run(args=_cmd, shell=True)

    LOG.info("\nInstalling 'uv' via pip.")
    _cmd = "pip install uv"
    subprocess.run(args=_cmd, shell=True)

    for _reponame in url_dict.keys():
        _repo_install_path = os.path.join(_setup_root, _reponame)
        # test for nested repos
        if "tirutils" in _reponame:
            _repo_install_path = os.path.join(_repo_install_path, "tirutils")
        if _reponame == "tirutils_plus":
            _repo_install_path += "_plus"

        _install_cmd = (
            f"cd {_repo_install_path} && uv pip install -r pyproject.toml --all-extras"
        )
        LOG.info(f"\nRepo '{_reponame}': installing dependencies from 'pyproject.toml'")
        subprocess.run(args=_install_cmd, shell=True)


def install_project_dependencies(_project_root: str):
    # now install 'pyproject.toml' from this repo
    LOG.info(f"\nRepo '{_project_root}': installing dependencies from 'pyproject.toml'")
    _cmd = "uv pip install -r pyproject.toml --all-extras && uv pip install --group dev"
    subprocess.run(args=_cmd, shell=True)

    # finally, setup pre-commit-hooks
    LOG.info(f"\nRepo '{_project_root}': installing pre-commit hooks")
    _cmd = "pre-commit install && pre-commit autoupdate"
    subprocess.run(args=_cmd, shell=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # create_conda_env(envname=test)
    # setup_git_repos(_project_root)
    install_project_dependencies(_project_root)
