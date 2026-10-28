from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
data = json.loads(contents)

print(f'welcome back {data}')
