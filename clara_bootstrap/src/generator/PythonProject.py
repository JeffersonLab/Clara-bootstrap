# coding=utf-8

from jinja import Environment, PackageLoader

from clara_bootstrap.src.utils.SystemUtils import *
from clara_bootstrap.src.res.Extras import LICENSE, GITIGNORE, README

env = Environment(loader=PackageLoader('clara_bootstrap',
                                       'src/res/templates'))


def create_init_file(path, template=None):
    init_file = open(path + "/__init__.py", "w")
    if template:
        init_template = env.get_template(template)
        init_file.write(init_template.render(author=get_username()))
    else:
        init_file.write("")
    init_file.close()


def create_python_service(project_name):
    service_name = project_name + "Service"
    package_folder = project_name + "/" + project_name + "/"
    test_folder = project_name + "/tests/"

    service_file_path = package_folder + service_name + ".py"
    test_file_path = test_folder + "test_" + service_name + ".py"

    # Create project folder
    create_folder(package_folder)
    create_folder(test_folder)

    # Create __init__.py
    create_init_file(package_folder, "services/python_init.txt")
    create_init_file(test_folder)

    # Create the service
    service_file = open(service_file_path, "w")
    service_template = env.get_template("services/python.txt")
    service_file.write(service_template.render(service_name=service_name))
    service_file.close()

    # Create tests
    test_file = open(test_file_path, "w")
    test_template = env.get_template("services/python_test.txt")
    test_file.write(test_template.render(project_name=project_name))
    test_file.close()


def create_python_setup(project_name):
    setup_file_path = project_name + "/setup.py"

    # Create setup.py
    template = env.get_template('setup/python_setup.txt')
    setup_file = open(setup_file_path, "w")
    setup_file.write(template.render(project_name=project_name,
                                     author=get_username()))
    setup_file.close()
    make_executable(project_name + "/setup.py")


def create_root_dir_extras(project_name):
    # README.md
    p_readme = open(project_name + "/README.md", "w")
    p_readme.write(README)
    p_readme.close()
    # LICENSE
    p_license = open(project_name + "/LICENSE", "w")
    p_license.write(LICENSE)
    p_license.close()
    # .gitignore
    p_gitignore = open(project_name + "/.gitignore", "w")
    p_gitignore.write(GITIGNORE)
    p_gitignore.close()


def create_python_project(project_name):

    if project_name:
        print "Creating the CLARA project skeleton..."
        create_python_service(project_name)
        create_python_setup(project_name)
        create_root_dir_extras(project_name)
        print "Project created."

    else:
        raise Exception("Project name is required for scaffolding...")
