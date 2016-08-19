# coding=utf-8

import os
import shutil
import subprocess
import tempfile

from git import Repo

from clara_bootstrap.utils.GeneralUtils import create_log_filename

GITHUB_REPO = "git@github.com:JeffersonLab/clara-python.git"


def _error_message(filename):
    return "\nSomething went wrong with the install\n" +\
           "Check the log at: " + filename


def install(repo=GITHUB_REPO):
    temp_dir = tempfile.gettempdir() + "/clara"
    log_file = open(create_log_filename("python_install"), "a")

    try:
        Repo.clone_from(repo, temp_dir)

        if not os.path.isdir(temp_dir):
            raise Exception("Could not create file...")

    except Exception as e:
        log_file.write(e.message)
        log_file.close()
        print _error_message(log_file.name)
        return -1

    os.chdir(temp_dir)

    try:
        print "[git_repo] cloning the latest version from github"
        subprocess.call(["pip", "install", "-r",
                         temp_dir + "/requirements.txt"],
                        stdout=log_file,
                        stderr=log_file)
        print "[python] Running ./setup.py install"
        subprocess.call(["python","setup.py", "install"],
                        stdout=log_file,
                        stderr=log_file)

    except Exception as e:
        log_file.write(e.message)
        log_file.close()
        print _error_message(log_file.name)
        return -1

    print "[python] Clara has been sucessfully installed in yout system..."
    shutil.rmtree(temp_dir)
