from pathlib import Path

try:
    cat_dir = Path("cat.txt")
    dog_dir = Path("dog.txt")
    cat_name = cat_dir.read_text(encoding="utf-8")
    dog_name = dog_dir.read_text(encoding="utf-8")

except FileNotFoundError:
    # print("file not fond")
    pass
else:
    print(cat_name)
    print(dog_name)
