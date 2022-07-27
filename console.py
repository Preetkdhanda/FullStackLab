# import pdb

from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author('Jack', 'Jones')
author_repository.save(author1)

author2 = Author('No', 'No')
author_repository.save(author2)



book1 = Book("Love", "Romance", "Penguin", author1)
book_repository.save(book1)

book2 = Book("Lover", "Romancer", "Penguinr", author2)
book_repository.save(book2)

results = book_repository.select_all()

for book in results:
    print(book.author.__dict__)


