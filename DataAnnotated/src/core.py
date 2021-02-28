import json

from ..constants.path import get_cache_path
from ..Utils.decorators import change_working_directory, cache_data

@change_working_directory
@cache_data
def show_datasets(*args, **kwargs):

    '''
    Lists all the datasets in the user profile
    '''

    data = kwargs['data']
    if data == None:
        print("Using Cached data...")
        with open('./dumps.json', 'r') as f:
            data = json.load(f)
    
    dataset_names = list()
    for task in data['annotation_data']:
        dataset_names.append(task["task_name"])
    
    return dataset_names 

def fetchDatasets():
    print("fetch datasets")

def parseDatasets():
    print("parse datasets")