# coding=utf-8

from jinja import Environment, PackageLoader

from clara_bootstrap.src.utils.SystemUtils import create_folder
from clara_bootstrap.src.res.Extras import LICENSE, GITIGNORE_JAVA, README

GRADLE_SRC_FOLDER = "/src/main/java"
GRADLE_RES_FOLDER = "/src/main/res"
GRADLE_TEST_FOLDER = "/src/test/java"

env = Environment(loader=PackageLoader("clara_bootstrap",
                                       "src/res/templates"))


def create_java_service(project_name):
    package_name = project_name + GRADLE_SRC_FOLDER + "/services/"
    test_folder = project_name + GRADLE_TEST_FOLDER
    res_folder = project_name + GRADLE_RES_FOLDER
    service_name = package_name + project_name + "Service.java"

    # Create project folders
    create_folder(package_name)
    create_folder(test_folder)
    create_folder(res_folder)

    # Create the service
    service_file = open(service_name, "w")
    service_template = env.get_template("services/java.txt")
    service_file.write(service_template.render(project_name=project_name))
    service_file.close()


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
    p_gitignore.write(GITIGNORE_JAVA)
    p_gitignore.close()


def create_java_project(project_name):

    if project_name:
        print "Creating the CLARA project skeleton..."
        create_java_service(project_name)
        # create_java_setup(project_name)
        create_root_dir_extras(project_name)
        print "Project created."

    else:
        raise Exception("Project name is required for scaffolding...")
