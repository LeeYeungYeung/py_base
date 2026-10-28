from pathlib import Path
import json


def get_luck_number(path):
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None


def greet_num():
    path = Path('luck_number.json')
    username = get_luck_number(path)
    if username:
        print(f'I know your luck number is: {username}')
    else:
        user_name = input("enter your luck number:\n")
        contents = json.dumps(user_name)
        path.write_text(contents)



greet_num()