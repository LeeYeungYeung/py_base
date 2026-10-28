from pathlib import Path

path = Path('learning_python.txt')

contents = path.read_text()
contents = contents.rstrip()
print(contents)

contents2 = contents.splitlines()
py_line = ''
for line in contents2:
    line = line.replace('py', 'c')
    py_line += line + ' '

print(py_line)
