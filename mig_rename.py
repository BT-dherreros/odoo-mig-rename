##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the AGPL-3.0 (http://www.gnu.org/licenses/agpl.html).
# See LICENSE file for full licensing details.
##############################################################################

import json
import os
import re
import sys
import argparse

NAME_CHANGES_CACHE = {}

def main(arguments):

    # Get arguments
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('module', help="Module")
    parser.add_argument('target_version', help="Target Version")


    # pick the rename_data.json
    my_dir = os.path.dirname(__file__)
    rename_data_json_path = os.path.join(my_dir, 'rename_data.json')

    # Load the name changes dictionary
    with open(rename_data_json_path, 'r') as name_changes_file:
        global NAME_CHANGES_CACHE
        NAME_CHANGES_CACHE = json.load(name_changes_file)

    args = vars(parser.parse_args(arguments))
    print(args)
    module_directory = args['module']
    target_version = args['target_version']
    # process the module by going through the module folder tree and renaming models and fields
    process_module(module_directory, target_version)
    print('Module {} has been processed. Its models and fields have been renamed to match their current names in'
          ' version {}'.format(module_directory, target_version))

def process_module(module_directory, target_version):
    start_version = get_start_version(module_directory)
    print('Processing of Module: {}. Manifest Starting Version: {}. Target Version: {}'.format(
        module_directory, start_version, target_version
    ))
    if not start_version:
        return False
    for root, dirs, files in os.walk(module_directory):
        for file in files:
            process_file(os.path.join(root, file), start_version, target_version)
    return True

def process_file(file, start_version, target_version):
    print('Starting Processing of File: {}'.format(file))
    with open(file, 'r', encoding='utf-8') as f:
        new_content = content = f.read()
    for version in range(int(start_version)+1, int(target_version)+1):
        # get model name changes for current version:
        version_name_changes = NAME_CHANGES_CACHE.get(str(version))
        if version_name_changes:
            # change model names
            print('Processing of File: {}. Name Changes found for version {}. Starting Renaming.'.format(
                file, version
            ))
            if version_name_changes.get('models'):
                for old_model_name, new_model_name in version_name_changes['models'].items():
                    new_content = re.sub(old_model_name, new_model_name, new_content)
            # change field names
            if version_name_changes.get('fields'):
                for model, fields in version_name_changes['fields'].items():
                    # We try to be sure we are changing the fields on the correct model file, of course, if a
                    # file has more than one model in it we are in deep trouble
                    if re.match(
                            r"_inherit\s*=\s*[\"']{}[\"']".format(model), new_content
                    ) or '<field name="model">{}</field>'.format(model) in new_content:
                        for old_field_name, new_field_name in fields.items():
                            new_content = re.sub(old_field_name, new_field_name, new_content)
            print('Processing of File: {}. Finished Renaming for version Changes found for version {}'.format(
                file, version
            ))
    if new_content != content:
        print('Processing of File: {}. Overwriting with updated content'.format(
            file, version
        ))
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return False

def get_start_version(module_directory):
    # Find the manifest file to get the start version
    start_version = ''
    try:
        with open(os.path.join(module_directory, '__manifest__.py'), 'r', encoding='utf-8') as f:
            content = f.read()
            version_pattern = r"'version':\s*'([^']+)'"
            version = re.search(version_pattern, content).group(1)
            start_version = version.split('.')[0]
    except ValueError as e:
        raise str(e)
    return start_version

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))