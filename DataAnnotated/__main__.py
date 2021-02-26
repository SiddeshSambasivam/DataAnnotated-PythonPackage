from __future__ import print_function

import webbrowser
from pyfiglet import figlet_format
from PyInquirer import prompt

from .Utils.utils import style, log
from .main import Login

def main():

    log("Data Annotated", color="blue", figlet=True)
    log("Welcome to DataAnnotated CLI", "green")

    questions = [
        {
            'type':'checkbox',
            'qmark': '😃',
            'message': '',
            'name': 'CLI Options',
            'choices':[
                {
                    'name':'Login',
                    'value':'Login'
                },
                {
                    'name':'Signup',
                    'value':'Signup'
                },
                {
                    'name':'Exit',
                    'value':'Exit'
                }
            ],
            'validate': lambda answer: 'You must one choose option only.' if (len(answer) == 0 or len(answer)>1) else True
        }
    ]

    answers = prompt(questions, style=style)

    if answers['CLI Options'][0] == "Login":
        Login()
    elif answers['CLI Options'][0] == "Signup":
        webbrowser.open_new("www.google.com")
    else:
        pass

if __name__ == "__main__":
    main()

# Basic check for login
    #  Basic Features
        # ShowDatasets()
            # List all the annotated datasets
        # push_datasets()
            # push dataset to the database
        # parseDatasets()
            # give the data in the format provided by the user

