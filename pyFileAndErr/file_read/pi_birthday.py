from pathlib import Path

path = Path('1-1000000/1-1000000.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input('Enter your birthday: ')
if birthday in pi_string:
    print('Your birthday appears more than once!')
else:
    print('Your birthday does not appears more than once!')