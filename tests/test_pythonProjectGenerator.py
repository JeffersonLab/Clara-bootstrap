# coding=utf-8

import os
import shutil
import unittest

from clara_bootstrap.src.generator.PythonProject import *

project_name = "TEST_PROJECT"
package_dir = project_name + "/" + project_name + "/"


class TestPythonProjectGenerator(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree(project_name)

    def test_create_python_service(self):
        create_python_service(project_name)
        self.assertTrue(os.path.exists(project_name))
        self.assertTrue(os.path.isfile(package_dir +
                                       "/__init__.py"))
        self.assertTrue(os.path.isfile(package_dir +
                                       "/TEST_PROJECTService.py"))

    def test_create_python_project(self):
        create_python_project(project_name)
        self.assertTrue(os.path.isfile(project_name + "/README.md"))
        self.assertTrue(os.path.isfile(project_name + "/LICENSE"))
        self.assertTrue(os.path.isfile(project_name + "/.gitignore"))
        self.assertTrue(os.path.isfile(project_name + "/setup.py"))
        self.assertTrue(os.path.isfile(project_name +
                                       "/tests/test_TEST_PROJECTService.py"))


if __name__ == "__main__":
    unittest.main()
