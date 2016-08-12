# coding=utf-8

import os
import unittest

from clara_bootstrap.src.utils.SystemUtils import *

FOLDER_NAME = "TEST_FOLDER"


class TestSystemUtils(unittest.TestCase):

    def setUp(self):
        create_folder(FOLDER_NAME)

    def tearDown(self):
        os.removedirs(FOLDER_NAME)
        self.assertFalse(os.path.exists(FOLDER_NAME))

    def test_get_username(self):
        self.assertIsInstance(get_username(), basestring)

    def test_create_folder(self):
        self.assertTrue(os.path.exists(FOLDER_NAME))


if __name__ == "__main__":
    unittest.main()
