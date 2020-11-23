import json
import jsonschema
from os import walk
import argparse


def main(json_files_path, schema_path, output_file):
    for step in walk(schema_path):  # make schema dictionary
        schemas_list = step[2]
    schemas = {key[:-7]: json.loads(value) for key in schemas_list for value in open('{}\{}'.format(schema_path, key))}

    for step in walk(json_files_path):  # make list of json files
        files = step[2]

    errors = {}

    for file in files:
        errors[file] = []
        with open('{}\{}'.format(json_files_path, file)) as f:
            jsonfile = json.load(f)
            if not jsonfile:
                errors[file].append('file is empty')
                continue
            if 'event' not in jsonfile or not jsonfile['event']:
                errors[file].append('schema property is absent')
                continue
            if 'data' not in jsonfile:
                errors[file].append('data property is absent')
                continue
            if jsonfile['event'] not in schemas:
                errors[file].append("schema " + jsonfile['event'] + " does not exist")
                continue
            try:
                jsonschema.validate(instance=jsonfile['data'], schema=schemas[jsonfile['event']])
            except jsonschema.exceptions.ValidationError as err:
                errors[file].append(err.message)


    with open(output_file, 'w') as output:
        for k, v in errors.items():
            print('File name: ' + k + ' List of errors: ' + str(*v), file=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-json_files_path', default='./event/', help='Folder, that store json files')
    parser.add_argument('-schema_path', default='./schema/', help='Folder, that store schemas')
    parser.add_argument('-err_file', default='./report.txt', help='File to store logs')

    argum = parser.parse_args()
    main(argum.json_files_path, argum.schema_path, argum.err_file)