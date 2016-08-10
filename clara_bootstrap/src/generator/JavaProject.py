# coding=utf-8

from clara_bootstrap.src.res.Extras import LICENSE, GITIGNORE_JAVA, README


def create_java_service(project_name):
    pass

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