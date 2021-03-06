# coding=utf-8

import subprocess

from clara_bootstrap.res.FileNameConstants import *
from clara_bootstrap.res.BaseConstants import LICENSE, GITIGNORE_JAVA,\
    README
from clara_bootstrap.utils.SystemUtils import *


def _create_java_service(project_name):
    package_name = project_name + GRADLE_SRC_FOLDER
    test_package_name = project_name + GRADLE_TEST_FOLDER
    service_name = package_name + project_name + "Service.java"
    service_name_test = test_package_name + project_name + "ServiceTest.java"

    # Create the service
    create_file_from_template(service_name,
                              TEMPLATE_JAVA_SERVICE,
                              project_name=project_name)

    create_file_from_template(service_name_test,
                              TEMPLATE_JAVA_TEST,
                              project_name=project_name)


def _create_java_setup(project_name):
    FNULL = open(os.devnull, 'w')
    subprocess.call(["gradle", "wrapper", "--project-dir", project_name],
                    stdout=FNULL, stderr=subprocess.STDOUT)
    create_file_from_template(project_name + GRADLE_FILE,
                              TEMPLATE_JAVA_SETUP,
                              project_name=project_name)
    copy_folder(JAVA_CONFIG_FOLDER, project_name + "/config")


def _create_root_dir(project_name):
    package_name = project_name + GRADLE_SRC_FOLDER
    test_folder = project_name + GRADLE_TEST_FOLDER
    res_folder = project_name + GRADLE_RES_FOLDER

    # Create project folders
    create_folder(package_name)
    create_folder(test_folder)
    create_folder(res_folder)
    # README.md
    create_file_from_string(project_name + README_FILE, README)
    # LICENSE
    create_file_from_string(project_name + LICENSE_FILE, LICENSE)
    # .gitignore
    create_file_from_string(project_name + GITIGNORE_FILE, GITIGNORE_JAVA)


def create_java_project(project_name):

    if project_name:
        print "Creating the CLARA Java project skeleton...\n"
        _create_root_dir(project_name)
        _create_java_setup(project_name)
        _create_java_service(project_name)
        print "\nProject created."

    else:
        raise Exception("Project name is required for scaffolding...")
