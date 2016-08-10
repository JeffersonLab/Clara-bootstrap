# coding=utf-8

import os
import unittest

from clara_bootstrap.src.generator.PythonProjectGenerator import *


class TestPythonProjectGenerator(unittest.TestCase):

    def test_create_python_service(self):
        project_name = "TEST_PROJECT"
        create_python_service(project_name)
        self.assertTrue(os.path.exists(project_name))
        self.assertTrue(os.path.isfile(project_name + "/YourService.py"))
        os.remove(project_name + "/YourService.py")

if __name__ == "__main__":
    unittest.main()
