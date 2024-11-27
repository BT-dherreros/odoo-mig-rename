# odoo-mig-rename

The idea behind this repository is to hold both the information of renames between Odoo versions and a script that runs
through a module changing those names between a base version (coming from the manifest file) and a target version
indicated by the user.

The JSON file rename_data.json holds the name changes per version.
The Python script mig_rename.py will take care of the renames.

The script is summoned as:
    python3 mig_rename.py <MODULE_PATH> <TARGET_VERSION>



TODOs:
- Increase coverage of rename_data.json
- Create unit tests. Comparing the result of processing test_module against manually migrated versions of it will give us better
understanding on the workings and possible issues per version change. 
- Cover the earliest versions of Odoo, if possible including ORM changes. (Maybe should be part of a different script)
- Update/Write file headers. This is a nice thing to have that would save some developing time. (Maybe should be part of a different script)
- For fields that have been renamed in a file that inherits a different model, we need to be able to identify
those case and rename accordingly. A example would be L25 of test_module/views/account_move.xml
- Cover of csv files. Since the naming of the models in the security csv files is different i.e. module.model_model_name,
we need to handle that different as with the simple replace we are doing for the python and xml files.
This will also help with other types of references in xml files i.e. XML IDs
Right now it 'kinda' works, because it finds and changes the values but it always change by dot separated, which
is not how it should be in XML IDs.
- Cleaner input/output logging, or logging at all :)
- Add progress bar
- Show diff files. This would be the lowest priority.
