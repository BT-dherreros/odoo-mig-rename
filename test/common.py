##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################

import os
import filecmp
import logging

logger = logging.getLogger()

def compare_folders(folder1, folder2):
    # Compare directory structure and file names
    comparison = filecmp.dircmp(folder1, folder2)

    # Check for mismatched files or directories
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False

    # Check file contents
    for filename in comparison.common_files:
        if not filecmp.cmp(os.path.join(folder1, filename), os.path.join(folder2, filename), shallow=False):
            return False

    # Recursively compare subdirectories
    for subdir in comparison.common_dirs:
        if not compare_folders(os.path.join(folder1, subdir), os.path.join(folder2, subdir)):
            return False

    return True