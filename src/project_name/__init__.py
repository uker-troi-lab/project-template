import os
import sys

_project_root = os.path.abspath(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../")
)
_setup_root = os.path.abspath(
    os.path.join(os.path.abspath(_project_root), "../")
)
_project_relative_dependencies = ["repo1", "repo2"]
_cur_path = sys.path
for _p in _project_relative_dependencies:
    _rel_deps_path = os.path.join(_setup_root, _p, "src")
    if not _rel_deps_path in _cur_path:
        sys.path.append(_rel_deps_path)
