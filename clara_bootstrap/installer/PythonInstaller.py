# coding=utf-8

import os
import shutil
import subprocess
import tempfile
from git import Repo

GITHUB_REPO = "https://github.com/JeffersonLab/clara-python"


def install():
    temp_dir = tempfile.gettempdir() + "/clara"
    exec_setup = temp_dir + "/setup.py"
    Repo.clone_from(GITHUB_REPO, temp_dir)
    if not os.path.isdir(temp_dir):
        raise Exception("Could not create file...")
    os.chdir(temp_dir)
    subprocess.call(["pip", "install", "-r", temp_dir + "/requirements.txt"])
    subprocess.call(["python","setup.py", "install"])
    shutil.rmtree(temp_dir)
