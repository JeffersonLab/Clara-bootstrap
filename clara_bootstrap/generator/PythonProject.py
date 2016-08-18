# coding=utf-8

from clara_bootstrap.res.FileNameConstants import *
from clara_bootstrap.res.BaseConstants import LICENSE, GITIGNORE, README
from clara_bootstrap.utils.SystemUtils import *


def _package_folder(project_name):
    return project_name + "/" + project_name + "/"


def _test_folder(project_name):
    return project_name + "/tests/"


def _create_python_service(project_name):
    service_name = project_name + "Service"
    service_file_path = _package_folder(project_name) + service_name + ".py"
    test_file_path = _test_folder(project_name) + "test_" + service_name + ".py"

    # Create the service
    create_file_from_template(service_file_path,
                              TEMPLATE_PYTHON_SERVICE,
                              service_name=service_name)

    # Create tests
    create_file_from_template(test_file_path,
                              TEMPLATE_PYTHON_TEST,
                              project_name=project_name)


def _create_python_setup(project_name):
    setup_file_path = project_name + "/setup.py"

    # Create setup.py
    create_file_from_template(setup_file_path,
                              TEMPLATE_PYTHON_SETUP,
                              project_name=project_name)
    make_executable(setup_file_path)


def _create_root_dir(project_name):
    # Create project folder
    create_folder(_package_folder(project_name))
    create_folder(_test_folder(project_name))

    # Create __init__.py
    create_file_from_template(_package_folder(project_name) + "__init__.py",
                              TEMPLATE_PYTHON_INIT,
                              author=get_username())
    create_file_from_string(_test_folder(project_name) + "__init__.py")

    # README.md
    create_file_from_string(project_name + README_FILE, README)
    # LICENSE
    create_file_from_string(project_name + LICENSE_FILE, LICENSE)
    # .gitignore
    create_file_from_string(project_name + GITIGNORE_FILE, GITIGNORE)


def create_python_project(project_name):

    if project_name:
        print "Creating the CLARA Python project skeleton...\n"
        _create_root_dir(project_name)
        _create_python_setup(project_name)
        _create_python_service(project_name)
        print "\nProject created."

    else:
        raise Exception("Project name is required for scaffolding...")
