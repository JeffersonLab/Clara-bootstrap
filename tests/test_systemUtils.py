# coding=utf-8

import os
import unittest

from clara_bootstrap.src.utils.SystemUtils import *


class TestSystemUtils(unittest.TestCase):

    def test_get_username(self):
        self.assertIsInstance(get_username(), basestring)

    def test_create_folder(self):
        folder_name = "TEST_FOLDER"
        create_folder(folder_name)
        self.assertTrue(os.path.exists(folder_name))
        os.removedirs(folder_name)
        self.assertFalse(os.path.exists(folder_name))

if __name__ == "__main__":
    unittest.main()
