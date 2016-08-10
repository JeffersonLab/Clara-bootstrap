# coding=utf-8

from jinja import Environment, PackageLoader

from clara_bootstrap.src.utils.SystemUtils import create_folder,get_username
from clara_bootstrap.src.res.Extras import LICENSE, GITIGNORE, README

env = Environment(loader=PackageLoader('clara_bootstrap',
                                       'src/res/templates'))


def create_python_service(project_name):
    # Create project folder
    create_folder(project_name + "/" + project_name)
    create_folder(project_name + "/tests")

    service_name = project_name + "Service"
    service_name_py = service_name + ".py"

    # Create the service
    service_file = open(project_name + "/"
                        + project_name + "/"
                        + service_name_py, "w")
    service_template = env.get_template('services/python.txt')
    service_file.write(service_template.render(service_name=service_name))
    service_file.close()

    # Create __init__.py
    init_file = open(project_name + "/"
                     + project_name + "/__init__.py", "w")
    init_template = env.get_template("services/python_init.txt")
    init_file.write(init_template.render(author=get_username()))
    init_file.close()


def create_python_setup(project_name):
    template = env.get_template('setup/python_setup.txt')
    file = open(project_name + "/setup.py", "w")
    file.write(template.render(project_name=project_name,
                               author=get_username()))
    file.close()


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
