import os
from pymongo import MongoClient
import yaml
import sys


def get_mongo_db_client():
    return MongoClient("mongodb+srv://{}:{}@{}.mongodb.net".format(
        os.environ['RESEARCHLY_MONGODB_USERNAME']
        , os.environ['RESEARCHLY_MONGODB_PASSWORD']
        , os.environ['RESEARCHLY_MONGODB_CLUSTER']
    ))


def get_mongo_db_db(path_config_file, environment):
    if not environment:
        environment = os.environ['ENVIRONMENT']
    with open(path_config_file, "r") as stream:
        try:
            db_names_env_mapping = yaml.safe_load(stream)
            db_name = db_names_env_mapping.get(environment)
            client = get_mongo_db_client()
            return client[db_name]
        except yaml.YAMLError as exc:
            print(exc)


def get_mongo_db_collection(collection_name, path_config_file, environment):
    return get_mongo_db_db(path_config_file, environment)[collection_name]


def check_collection_exist(path_db_config_file, environment, collection_to_test):
    db = get_mongo_db_db(path_db_config_file, environment)
    available_collections = db.list_collection_names()
    if collection_to_test not in available_collections:
        print(f'{collection_to_test} not in available_collections. These are available:')
        print('\n'.join(available_collections))
        print('Aborting')
        sys.exit()
