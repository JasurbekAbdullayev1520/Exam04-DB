
from datetime import datetime
from sqlalchemy import DateTime
from library.create_tables import init_db
from library.services import (
    create_author,
    create_book,
    get_all_authors,
    get_all_books,
    get_author_by_id,
    get_book_by_id,
    search_books_by_title,
    delete_author,
    delete_book,
    update_author
)

init_db()

# # Mualliflar yaratish
# create_author(name="xexa xexu", bio="exaxa uxaxaxaxaxa")
# print('Muallif yaratildi.')

# Kitoblar yaratish
# create_book(title="exam04 dagi azoblar", author_id=1, published_year=2020, isbn="1234567890123")
# print('Kitob yaratildi.')

# Barcha mualliflarni olish
# authors = get_all_authors()
# for author in authors:
#     print(author)
    
# Barcha kitoblarni olish
# books = get_all_books()
# for book in books:
#     print(book)

# update_author(4, name='nimadir')
# print(get_author_by_id(4))

# # ID bo'yicha muallifni olish
# author = get_author_by_id(author_id=1)
# print(author)

# # # ID bo'yicha kitobni olish
# book = get_book_by_id(book_id=1)
# print(book)

# # # Sarlavha bo'yicha kitoblarni qidirish
# books = search_books_by_title(title="azob")
# for book in books:
#     print(book)

# # Muallifni o'chirish
# success = delete_author(author_id=10)
# if success:
#     print("Muallif o'chirildi.")
# # # Kitobni o'chirish
# success = delete_book(book_id=1)    
# if success:
#     print("Kitob o'chirildi.")
# else:
#     print("Kitobni o'chirish mumkin emas.")mport get_db


