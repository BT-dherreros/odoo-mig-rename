##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################

import os
import unittest
import subprocess

from common import compare_folders

class TestMigrationRenaming14(unittest.TestCase):

    def setUp(self):
        # Change root directory
        self.original_dir = os.getcwd()
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # Define paths or any setup needed
        self.script_path = 'mig_rename.py'
        self.module_directory = 'test/data/module_test'
        self.target_version = '14'
        self.expected_file_result = 'test/data/module_test'

    def tearDown(self):
        # Revert to the original working directory
        os.chdir(self.original_dir)

    def test_script_with_arguments(self):
        # Command to execute the script with arguments
        command = ['python3', self.script_path, self.module_directory, self.target_version]

        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

        # Assert statements to check if the output is as expected
        # loop test_module_14 to see if the processed output is correct
        folder1 = "test/data/module_test"
        folder2 = "test/data/result_test/result_14_test"
        self.assertTrue(compare_folders(folder1, folder2), "Folders are not identical!")



if __name__ == '__main__':
    unittest.main()
