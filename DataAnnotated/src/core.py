import os
import requests
import json

from ..Utils.api import download_data, GET_FETCH_API
from ..constants.path import get_cache_path

def show_datasets(refresh:bool=False):

    path = get_cache_path()
    os.chdir(path)

    if not 'jwt.json' in os.listdir("./"):
        raise EnvironmentError("User not logged in. Please login using the package CLI.")

    def cache_data() -> dict:

        url = GET_FETCH_API()
        
        with open("./jwt.json") as f:
            data = json.load(f)
            jwt = data['data']["token"]

        payload={}
        headers = {
        'auth-token': jwt
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        with open("./dumps.json", "w+") as f:
            data = response.json()["data"]['user']
            json.dump(data,f,indent=2)

        return data

    if not refresh:

        try:

            with open('./dumps.json', 'r') as f:
                data = json.load(f)

        except: 

            data = cache_data()
    
    else:

        data = cache_data()
    
    dataset_names = list()
    for task in data['annotation_data']:
        dataset_names.append(task["task_name"])
    
    return dataset_names
        


def fetchDatasets():
    print("fetch datasets")

def parseDatasets():
    print("parse datasets")