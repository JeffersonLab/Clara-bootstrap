# coding=utf-8

import os
import shutil
import unittest

from clara_bootstrap.installer.PythonInstaller import install


class TestPythonProjectInstaller(unittest.TestCase):

    def tearDown(self):
        pass

    def test_create_python_project(self):
        install()


if __name__ == "__main__":
    unittest.main()
