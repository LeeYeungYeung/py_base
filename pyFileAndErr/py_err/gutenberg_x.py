from pathlib import Path

book_path = Path(__file__)

book_text_count = book_path.read_text().count('hello')
print(book_text_count)
