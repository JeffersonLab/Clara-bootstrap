# coding=utf-8

from jinja import Environment, PackageLoader

from clara_bootstrap.src.utils.SystemUtils import *
from clara_bootstrap.src.res.BaseConstants import LICENSE, GITIGNORE, README

env = Environment(loader=PackageLoader('clara_bootstrap',
                                       'src/res/templates'))


def _package_folder(project_name):
    return project_name + "/" + project_name + "/"


def _test_folder(project_name):
    return project_name + "/tests/"


def create_init_file(path, template=None):
    init_file = open(path + "__init__.py", "w")
    if template:
        init_template = env.get_template(template)
        init_file.write(init_template.render(author=get_username()))
    else:
        init_file.write("")
    verify_file_creation(init_file.name)
    init_file.close()


def create_python_service(project_name):
    service_name = project_name + "Service"

    service_file_path = _package_folder(project_name) + service_name + ".py"
    test_file_path = _test_folder(project_name) + "test_" + service_name + ".py"

    # Create the service
    service_file = open(service_file_path, "w")
    service_template = env.get_template("services/python.txt")
    service_file.write(service_template.render(service_name=service_name))
    service_file.close()
    verify_file_creation(service_file.name)

    # Create tests
    test_file = open(test_file_path, "w")
    test_template = env.get_template("services/python_test.txt")
    test_file.write(test_template.render(project_name=project_name))
    test_file.close()
    verify_file_creation(test_file.name)


def create_python_setup(project_name):
    setup_file_path = project_name + "/setup.py"

    # Create setup.py
    template = env.get_template('setup/python_setup.txt')
    setup_file = open(setup_file_path, "w")
    setup_file.write(template.render(project_name=project_name,
                                     author=get_username()))
    setup_file.close()
    verify_file_creation(setup_file.name)
    make_executable(project_name + "/setup.py")


def create_root_dir(project_name):
    # Create project folder
    create_folder(_package_folder(project_name))
    create_folder(_test_folder(project_name))

    # Create __init__.py
    create_init_file(_package_folder(project_name), "services/python_init.txt")
    create_init_file(_test_folder(project_name))

    # README.md
    p_readme = open(project_name + "/README.md", "w")
    p_readme.write(README)
    p_readme.close()
    verify_file_creation(p_readme.name)
    # LICENSE
    p_license = open(project_name + "/LICENSE", "w")
    p_license.write(LICENSE)
    p_license.close()
    verify_file_creation(p_license.name)
    # .gitignore
    p_gitignore = open(project_name + "/.gitignore", "w")
    p_gitignore.write(GITIGNORE)
    p_gitignore.close()
    verify_file_creation(p_gitignore.name)


def create_python_project(project_name):

    if project_name:
        print "Creating the CLARA project skeleton..."
        create_root_dir(project_name)
        create_python_setup(project_name)
        create_python_service(project_name)
        print "Project created."

    else:
        raise Exception("Project name is required for scaffolding...")
