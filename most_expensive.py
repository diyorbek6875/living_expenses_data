import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    m=open('data.json')
    x=json.load(m)
    y=max(x.values())
    return y


# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)