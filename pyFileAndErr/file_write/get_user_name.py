from pathlib import Path

path = Path("guers.txt")
user_list=''
user = input("Enter your username:\n")
while user:
    user_list += user + '\n'
    user = input("please enter your:\n")

path.write_text(user_list)
