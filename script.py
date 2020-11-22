import json
from jsonschema import validate
from os import walk


def main():
    for step in walk('schema'):  # make schema dictionary
        schemas_list = step[2]
    schemas = {key[:-7]: value for key in schemas_list for value in open('.\schema\{}'.format(key))}

    for step in walk('event'):  # make list of json files
        files = step[2]

    for file in files:
        with open('.\event\{}'.format(file)) as f, open('err_logs\err_log_{}.txt'.format(file), 'w') as log:
            jsonfile = json.load(f)
            try:
                schema_name = jsonfile['event']
            except (TypeError, KeyError):
                log.write('schema is absent' + '\n')
            try:
                data_to_validate = jsonfile['data']
            except (TypeError, KeyError):
                log.write('data is absent' + '\n')
            try:
                validate(data_to_validate, schemas[schema_name])
            except TypeError as err:
                log.write(str(err))
            except KeyError as err:
                log.write("schema " + str(err) + " does not exist")


if __name__ == "__main__":
    main()