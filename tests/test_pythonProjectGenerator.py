# coding=utf-8

import os
import shutil
import unittest

from clara_bootstrap.src.generator.PythonProject import *

project_name = "TEST_PROJECT"
src_file_path = "TEST_PROJECT/TEST_PROJECT/"
test_file_path = "TEST_PROJECT/tests/"


class TestPythonProjectGenerator(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree(project_name)

    def test_create_python_project(self):
        create_python_project(project_name)
        self.assertTrue(os.path.isfile(project_name + "/README.md"))
        self.assertTrue(os.path.isfile(project_name + "/LICENSE"))
        self.assertTrue(os.path.isfile(project_name + "/.gitignore"))
        self.assertTrue(os.path.isfile(project_name + "/setup.py"))
        self.assertTrue(os.path.isfile(src_file_path + "__init__.py"))
        self.assertTrue(os.path.isfile(test_file_path + "__init__.py"))
        self.assertTrue(os.path.isfile(src_file_path +
                                       "TEST_PROJECTService.py"))
        self.assertTrue(os.path.isfile(test_file_path +
                                       "test_TEST_PROJECTService.py"))


if __name__ == "__main__":
    unittest.main()
