# welltory-test

## Assumptions
"script.py" is a python module made to validate json file with given schemas.
Validation is going according to field "data", the corresponding schema is taken from the field "event".

## Requirements 
python 3 with installed "jsonschema" module.

## Usage
To run the script it's possible to assign:
Folder, that store json files (json_files_path), by default='./task_folder/event/',
Folder, that store schemas (schema_path), by default='./task_fodelr/schema/',
File to store logs (err_file), by default='./report.txt'.

## Output:
file with a list of errors, made by template:
'File name: + List of errors: ', every new file on a new line.
If list of errors is empty - json file is OK.
### Example:
File name: 6b1984e5-4092-4279-9dce-bdaa831c7932.json List of errors: ["schema 'meditation_created' does not exist"]
