# coding=utf-8

from jinja import Environment, PackageLoader

from clara_bootstrap.src.utils.SystemUtils import create_folder

env = Environment(loader=PackageLoader('clara_bootstrap',
                                       'src/res/templates/services'))


def create_python_service(project_name):
    create_folder(project_name)
    template = env.get_template('python.txt')
    file = open(project_name + "/YourService.py", "w")
    file.write(template.render(service_name="YourClassName"))
    file.close()
