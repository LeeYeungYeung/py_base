from pathlib import Path


def count_words(file_path):
    try:
        contents = file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {file_path} has about {num_words} words')


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_woment.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
