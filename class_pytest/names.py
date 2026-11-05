from name_function import get_formatted_name

print("enter 'q' to quit")
while True:
    first_name = input("first name: ")
    if first_name == "q":
        break
    last_name = input("last name: ")
    if last_name == "q":
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(formatted_name)