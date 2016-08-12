# coding=utf-8

import os
import shutil
import unittest

from clara_bootstrap.src.generator.JavaProject import create_java_project

project_name = "TEST_PROJECT"
src_file_path = "TEST_PROJECT/src/main/java/services/TEST_PROJECTService.java"
test_file_path = "TEST_PROJECT/src/test/java/services/" \
                 "TEST_PROJECTServiceTest.java"


class TestJavaProjectGenerator(unittest.TestCase):

    def tearDown(self):
        shutil.rmtree(project_name)

    def test_create_java_project(self):
        create_java_project(project_name)
        self.assertTrue(os.path.isdir(project_name + "/config"))
        self.assertTrue(os.path.isfile(project_name + "/build.gradle"))
        self.assertTrue(os.path.isfile(project_name + "/gradlew"))
        self.assertTrue(os.path.isfile(project_name + "/gradlew.bat"))
        self.assertTrue(os.path.isfile(project_name + "/README.md"))
        self.assertTrue(os.path.isfile(project_name + "/README.md"))
        self.assertTrue(os.path.isfile(project_name + "/LICENSE"))
        self.assertTrue(os.path.isfile(project_name + "/.gitignore"))
        self.assertTrue(os.path.isfile(src_file_path))
        self.assertTrue(os.path.isfile(test_file_path))


if __name__ == "__main__":
    unittest.main()
