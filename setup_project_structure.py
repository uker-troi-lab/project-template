import os
import logging
LOG = logging.getLogger(__name__)

# this files ensures to setup the expected development-repo-structure
# please adjust also ./src/{project_name}/__init__.py accordingly to 
# make sure the dependencies on relative paths are added to the PATH
# environment variable.

def setup_git_repos():
    logging.basicConfig(level=logging.INFO)
    url_dict = {
        "repo1": 'https://url-to-git-host.com/repo1.git',
        "repo2": 'https://url-to-git-host.com/repo2.git',
    }
    _project_root = os.path.abspath(os.path.dirname(__file__))
    _setup_root = os.path.abspath(
        os.path.join(_project_root, "../")
    )
    LOG.info(f"setup_root: {_setup_root}")
    
    for _reponame, _repourl in url_dict.items():
        git_path = os.path.join(_setup_root, _reponame)
        if not os.path.isdir(git_path):
            LOG.warning(f"'{_reponame}' does not exist - downloading it.")
            os.system("git clone " + _repourl + " " + git_path)
        else:
            # pull latest version
            LOG.info(f"'{_reponame}' already exists - pulling latest version.")
            os.system("cd " + git_path + " && git pull")

    LOG.info("\nInstalling 'uv' via pip.")
    os.system('pip install uv')
    
    for _reponame in url_dict.keys():
        _install_cmd = (
            'cd '            
            f'{os.path.join(_setup_root, _reponame)} && '
            'uv pip install -r pyproject.toml"'
        )
        LOG.info(f"\nRepo '{_reponame}': installing dependencies from 'pyproject.toml'")
        os.system(_install_cmd)
    
    # now install 'pyproject.toml' from this repo
    LOG.info(f"\nRepo '{_project_root}': installing dependencies from 'pyproject.toml'")
    os.system('uv pip install -r pyproject.toml"')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    setup_git_repos()
