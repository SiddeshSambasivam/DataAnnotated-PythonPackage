from __future__ import print_function

import re
import six
from pyfiglet import figlet_format
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt, style_from_dict)

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


style = style_from_dict({
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})

def log(string, color, figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string), color))
    else:
        six.print_(string)

class EmailValidator(Validator):
    pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"

    def validate(self, email) -> bool:
        if len(email.text):
            if re.match(self.pattern, email.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid email",
                    cursor_position=len(email.text))
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(email.text))

class PasswordValidator(Validator):

    def validate(self, password) -> bool:
        
        if not len(password.text):
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(password.text))

        return True

def search(annotation_data:list, task_name:str):
    '''
    Searches the annotation data for the given task name
    '''

    for data in annotation_data:

        if data['task_name'] == task_name:
            return data
        
    return -1
