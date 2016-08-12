# coding=utf-8

import getpass
import os
import shutil

from jinja import Environment, PackageLoader


env = Environment(loader=PackageLoader("clara_bootstrap", "src/res/templates"))


def copy_folder(origin_path, destination_path):
    # Check if destination folder exists
    dir = os.path.dirname(__file__)
    origin_path = os.path.join(dir, origin_path)
    if not os.path.isdir(destination_path):
        shutil.copytree(origin_path, destination_path)
    _verify_file_creation(destination_path)


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def get_username():
    """Returns the active username"""
    return getpass.getuser()


def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)
    print "executable:\t" + path


def create_file_from_string(file_path, content_string=""):
    file_object = open(file_path, "w")
    file_object.write(content_string)
    file_object.close()
    _verify_file_creation(file_object.name)


def create_file_from_template(file_path, template, **kwargs):
    file_object = open(file_path, "w")
    service_template = env.get_template(template)
    file_object.write(service_template.render(kwargs))
    file_object.close()
    _verify_file_creation(file_object.name)


def _verify_file_creation(filename):
    if os.path.isfile(filename) or os.path.isdir(filename):
        print "created:\t" + filename
    else:
        raise IOError("Could not create file")