from pathlib import Path
import json

path = Path('number.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
