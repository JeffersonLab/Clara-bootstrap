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


def install(repo=GITHUB_REPO, install_dir=None):
    preserve_install = True if install_dir else False
    install_dir = install_dir or tempfile.gettempdir()
    log_file = open(create_log_filename("python_install"), "a")

    try:
        install_dir = os.path.join(install_dir, "clara-python")
        Repo.clone_from(repo, install_dir)

        if not os.path.isdir(install_dir):
            raise Exception("Could not create file...")

    except Exception as e:
        log_file.write(e.message)
        log_file.close()
        print _error_message(log_file.name)
        return -1
    cur_dir = os.getcwd()
    os.chdir(install_dir)

    try:
        print "[git_repo] cloning the latest version from github"
        subprocess.call(["pip", "install", "-r",
                         install_dir + "/requirements.txt"],
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

    # cleaning up
    if not preserve_install:
        shutil.rmtree(install_dir)
    os.chdir(cur_dir)
    if os.path.isfile(log_file.name):
        os.remove(log_file.name)
