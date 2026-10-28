from pathlib import Path
import json

numners = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

path = Path('number.json')
contents = json.dumps(numners)
path.write_text(contents)
