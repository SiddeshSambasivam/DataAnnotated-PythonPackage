import os
import functools
import inspect
import json
import requests

from ..constants.path import get_cache_path
from ..Utils.api import GET_FETCH_API

def cache_data(func):
    '''
    Caches the user data from the database to the local environment
    '''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if not 'jwt.json' in os.listdir("./"):
            raise EnvironmentError("User not logged in. Please login using the package CLI.")

        refresh, data = kwargs.get('refresh'), None
        if refresh == None:
            try:
                if args[0] == True:
                    refresh = True

                refresh = False
            except IndexError:
                # Set to default value
                refresh= False

        if refresh or not os.path.exists("dumps.json"):
            url = GET_FETCH_API()
            
            with open("./jwt.json") as f:
                data = json.load(f)
                jwt = data['data']["token"]

            payload={}
            headers = {
            'auth-token': jwt
            }

            print("Downloading fresh data...")
            response = requests.request("GET", url, headers=headers, data=payload)
            with open("./dumps.json", "w+") as f:
                data = response.json()["data"]['user']
                json.dump(data,f,indent=2)            

        dataset_names = func(*args, **kwargs, data=data)
        return dataset_names

    return wrapper

def change_working_directory(func):
    '''
    Changes the working directory to the local cache directory
    '''    

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        path = get_cache_path()
        os.chdir(path)

        return func(*args, **kwargs)
    
    return wrapper







