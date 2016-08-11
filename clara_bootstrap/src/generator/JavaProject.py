# coding=utf-8

import subprocess

from clara_bootstrap.src.utils.SystemUtils import *
from clara_bootstrap.src.res.BaseConstants import LICENSE, GITIGNORE_JAVA, README

GRADLE_SRC_FOLDER = "/src/main/java"
GRADLE_RES_FOLDER = "/src/main/res"
GRADLE_TEST_FOLDER = "/src/test/java"


def _create_java_service(project_name):
    package_name = project_name + GRADLE_SRC_FOLDER + "/services/"
    service_name = package_name + project_name + "Service.java"

    # Create the service
    create_file_from_template(service_name,
                              "services/java.txt",
                              project_name=project_name)


def _create_java_setup(project_name):
    subprocess.call(["gradle", "wrapper", "--project-dir", project_name])
    create_file_from_template(project_name + "/build.gradle",
                              "setup/java_setup.txt",
                              project_name=project_name)


def _create_root_dir(project_name):
    package_name = project_name + GRADLE_SRC_FOLDER + "/services/"
    test_folder = project_name + GRADLE_TEST_FOLDER
    res_folder = project_name + GRADLE_RES_FOLDER

    # Create project folders
    create_folder(package_name)
    create_folder(test_folder)
    create_folder(res_folder)
    # README.md
    create_file_from_string(project_name + "/README.md", README)
    # LICENSE
    create_file_from_string(project_name + "/LICENSE", LICENSE)
    # .gitignore
    create_file_from_string(project_name + "/.gitignore", GITIGNORE_JAVA)


def create_java_project(project_name):

    if project_name:
        print "Creating the CLARA project skeleton...\n"
        _create_root_dir(project_name)
        _create_java_setup(project_name)
        # create_java_service(project_name)
        print "\nProject created."

    else:
        raise Exception("Project name is required for scaffolding...")
