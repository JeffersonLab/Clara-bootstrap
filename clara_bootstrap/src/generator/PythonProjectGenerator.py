# coding=utf-8

from jinja import Environment, PackageLoader

from clara_bootstrap.src.utils.SystemUtils import create_folder
from clara_bootstrap.src.res.Extras import LICENSE, GITIGNORE, README

env = Environment(loader=PackageLoader('clara_bootstrap',
                                       'src/res/templates/services'))


def create_python_service(project_name):
    create_folder(project_name)
    template = env.get_template('python.txt')
    file = open(project_name + "/YourService.py", "w")
    file.write(template.render(service_name="YourClassName"))
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


def create_project(project_name="bla"):
    create_python_service(project_name)
    create_root_dir_extras(project_name)
