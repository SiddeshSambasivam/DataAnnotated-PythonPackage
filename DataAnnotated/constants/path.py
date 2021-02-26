from appdirs import *

PACKAGE_NAME = "DataAnnotated"
PACKAGE_AUTHOR = "Siddesh Sambasivam Suseela"

def get_cache_path():

    return user_data_dir(PACKAGE_NAME, PACKAGE_AUTHOR)
