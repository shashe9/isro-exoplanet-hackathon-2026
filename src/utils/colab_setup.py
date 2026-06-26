"""
Colab environment setup.

Every notebook should call:

from src.utils.colab_setup import setup_environment

setup_environment()
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


REPO_NAME = "isro-exoplanet-hackathon-2026"
GITHUB_USERNAME = "shashe9"


def setup_environment():
    """
    Prepare the notebook environment.
    """

    repo_path = Path(f"/content/{REPO_NAME}")

    # Clone repository if missing
    if not repo_path.exists():
        subprocess.run(
            [
                "git",
                "clone",
                f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
            ],
            check=True
        )

    # Add project root to Python path
    if str(repo_path) not in sys.path:
        sys.path.insert(0, str(repo_path))

    print("Project ready.")