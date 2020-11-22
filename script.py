import json
from jsonschema import validate
from os import walk


def main(json_files_path, schema_path):
    for step in walk(schema_path):  # make schema dictionary
        schemas_list = step[2]
    schemas = {key[:-7]: value for key in schemas_list for value in open('{}\{}'.format(schema_path, key))}

    for step in walk(json_files_path):  # make list of json files
        files = step[2]

    errors = {}

    for file in files:
        errors[file] = []
        with open('{}\{}'.format(json_files_path, file)) as f:
            jsonfile = json.load(f)
            try:
                schema_name = jsonfile['event']
            except (TypeError, KeyError):
                errors[file].append('schema property is absent')
            try:
                data_to_validate = jsonfile['data']
            except (TypeError, KeyError):
                errors[file].append('data property is absent')
            try:
                validate(data_to_validate, schemas[schema_name])
            except TypeError as err:
                errors[file].append(str(err))
            except KeyError as err:
                errors[file].append("schema " + str(err) + " does not exist")

    with open('README.txt', 'w') as readme:
        for k, v in errors.items():
            print('File name: ' + k + ' List of errors: ' + str(v), file=readme)


if __name__ == "__main__":
    main(input("Please enter path to folder with json files: "), input("Please enter path to folder with schemas: "))
