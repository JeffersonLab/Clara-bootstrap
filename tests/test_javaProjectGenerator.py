# coding=utf-8

import os
import shutil
import unittest

from clara_bootstrap.src.generator.JavaProject import create_java_project

project_name = "TEST_PROJECT"
src_dir = project_name + "/src/main/java/"
test_dir = project_name + "/src/test/java"


class TestJaveProjectGenerator(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree(project_name)

    def test_create_java_project(self):
        create_java_project(project_name)
        self.assertTrue(os.path.isfile(project_name + "/README.md"))
        self.assertTrue(os.path.isfile(project_name + "/LICENSE"))
        self.assertTrue(os.path.isfile(project_name + "/.gitignore"))


if __name__ == "__main__":
    unittest.main()
