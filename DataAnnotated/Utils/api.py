
def GET_AUTH_API(email:str, password:str) -> str:
    return f"https://data-annotated.herokuapp.com/api/user/login?email={email}&password={password}"

def GET_FETCH_API() -> str:

    return "https://data-annotated.herokuapp.com/api/fetchData"

def download_data():
    pass