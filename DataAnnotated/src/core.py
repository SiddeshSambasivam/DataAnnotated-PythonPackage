import json

from ..constants.path import get_cache_path
from ..Utils.decorators import change_working_directory, cache_data
from ..Utils.utils import search
from .text import TextEntityAnnotation

TASK_TYPE = {
    'TextEntityAnnotation':TextEntityAnnotation
}

@change_working_directory
@cache_data
def list_datasets(*args, **kwargs):

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

@change_working_directory
@cache_data
def show_dataset(dataset_name:str, samples:int=1,*args, **kwargs):

    with open('./dumps.json', 'r') as f:
        user_data = json.load(f)

    user_dataset = search(user_data['annotation_data'], dataset_name)

    if user_dataset == -1:
        raise ValueError("Dataset not found. Check dataset name or recache the environment with `show_datasets(refresh=True)`")

    task = TASK_TYPE[user_dataset['task_type']](user_dataset)

    sents, ets  = task.get_dataset(samples)
    for i, (tokens, labels) in enumerate(zip(sents, ets)):        
        print(f"Sample {i}")
        print(*tokens)
        print(*labels)
        print()

@change_working_directory
@cache_data
def get_dataset(dataset_name:str, *args, **kwargs):

    with open('./dumps.json', 'r') as f:
        user_data = json.load(f)

    user_dataset = search(user_data['annotation_data'], dataset_name)

    if user_dataset == -1:
        raise ValueError("Dataset not found. Check dataset name or recache the environment with `show_datasets(refresh=True)`")

    task = TASK_TYPE[user_dataset['task_type']](user_dataset)

    return task

    