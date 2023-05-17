import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    f=open('data.json')
    x=json.load(f)
    a=0
    b=0
    for i in x.values():
        b+=i
        a+=i
    return b/a


# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
