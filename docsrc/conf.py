"""Sphinx configuration for GEOMETOR • hilbert."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.hilbert as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "hilbert"
repo_name = "hilbert"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • hilbert"
author = "David Hilbert"
copyright = "1899 B. G. Teubner · 1902 Open Court · Digital Codex GEOMETOR"

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/hilbert/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/hilbert/index.rst")  # noqa: F405

# Register offline-first local intersphinx inventories across the GEOMETOR historical canon
for _sister_repo in ("euclid", "elements", "hoenen", "pappus"):
    _local_inv = (_WORKSPACE_ROOT / _sister_repo / "docs" / "objects.inv").resolve()
    if _local_inv.is_file():
        intersphinx_mapping[_sister_repo] = (  # noqa: F405
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )
