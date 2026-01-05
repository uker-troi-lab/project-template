import os
import sys
import importlib.metadata

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for development mode

_project_root = os.path.abspath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../")
)
_setup_root = os.path.abspath(os.path.join(os.path.abspath(_project_root), "../"))
_project_relative_dependencies = ["repo1", "repo2"]
_cur_path = sys.path
for _p in _project_relative_dependencies:
    _rel_deps_path = os.path.join(_setup_root, _p, "src")
    if _rel_deps_path not in _cur_path:
        if not os.path.exists(_rel_deps_path):
            raise Exception(
                f"{_rel_deps_path} does not exist; "
                "please clone the repo first before running the tests."
            )
        else:
            sys.path.append(_rel_deps_path)
