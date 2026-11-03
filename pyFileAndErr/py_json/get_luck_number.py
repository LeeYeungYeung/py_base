from pathlib import Path
import json


def get_favorite_number(path):
    if path.exists():
        content = path.read_text()
        data = json.loads(content)
        return data
    else:
        return None


def print_favorite_number():
    path = Path('luck_numbers.json')
    number = get_favorite_number(path)
    if number:
        print(f"I know your favorite number: It's {number}")
    else:
        number = input("Please enter your favorite number: ")
        contents = json.dumps(number)
        path.write_text(contents)

