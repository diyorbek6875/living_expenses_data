import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    f=open('data.json')
    x=json.load(f)
    return x
# test
file_path = "data.json"
data = get_data(file_path)
print(data)
