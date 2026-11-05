from name_function import get_formatted_name

def test_first_lase_name():
    formatted_name = get_formatted_name("john", "joplin")
    assert formatted_name == "janis Joplin"
