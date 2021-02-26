from __future__ import print_function

import os
import json
import requests

from pyfiglet import figlet_format
from PyInquirer import prompt

from .Utils.utils import style, log, EmailValidator, PasswordValidator
from .Utils.api import GET_AUTH_API
from .constants.path import get_cache_path

def authenticate(email:str, password:str):

    url = GET_AUTH_API(email, password)

    payload={}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.json().get("error"):
        error = response.json().get("error")
        log(f"{error}. Try again", "red")
        Login()
    
    path = get_cache_path()
    
    try:
        os.chdir(path)
    except FileNotFoundError:
        os.makedirs(path)
        os.chdir(path)

    with open("jwt.json", "w") as outfile:
        json.dump(response.json(), outfile, indent=2)

    log(f"Successful Authentication. You may start using the python package 😃","green")


def Login():
    
    questions = [
        {
            'type': 'input',
            'name': 'email',
            'message':'Email',
            'validate':EmailValidator
        },
        {
            'type': 'input',
            'name': 'password',
            'message':'Password',
            'validate': PasswordValidator
        },        
        {
            'type': 'confirm',
            'name': 'Confirm',
            'message': 'Confirm'
        }
    ]

    answers = prompt(questions, style=style)
    authenticate(answers['email'], answers['password'])
    
    
