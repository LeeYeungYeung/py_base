from pathlib import Path
import json


def get_user_info(path,name=None):
    if path.exists():
        contents = path.read_text()
        print(contents)
        try:
            user = json.loads(contents)
            if user['username'] == name:
                return user
            else:
                return None
        except ValueError:
            pass
        return None
    else:
        return None


def greet_num():
    path = Path('luck_number.json')
    login_user = input("please enter your username:\n")

    user = get_user_info(path,login_user)
    if user:
        print(f'your info : {user}')
    else:
        user_name = input("enter your name:\n")
        user_age = input("enter your  age:\n")
        user_num = input("enter your luck number:\n")
        user = {
            'username': user_name,
            'age': user_age,
            'luck_number': user_num
        }
        contents = json.dumps(user)
        path.write_text(contents)


greet_num()
