# test.py (service.py dagi haqiqiy nomlarga moslangan)

from datetime import datetime
from library.create_tables import init_db
from library.services import (
    create_author, get_author_by_id, get_all_authors, update_author, delete_author,
    create_book, get_book_by_id, get_all_books, search_books_by_title, delete_book,
    create_student, get_student_by_id, get_all_students, update_student_grade,
    borrow_book, return_book,
    get_books_by_author, get_student_borrow_count, get_currently_borrowed_books, get_overdue_borrows
)


init_db()





#----------4ta table uchun obyektlar yaratish---------------------


# author1 = create_author("Ali", "Bio 1")
# author2 = create_author("Vali", "Bio 2")



# #---------------------AUTHOR TESTS---------------------------------

# author1 = create_author("Alisher Navoi", "G`azal mulkining sultoni")
# author2 = create_author("Muhammad Yusuf", "Sheriy to`plamlar egasi")

# result = get_author_by_id(1)
# print("GET AUTHOR:", result)

# delete_author(2)
# print("AFTER DELETE AUTHOR:", get_author_by_id(2))

# r = get_all_authors()
# print(r)



# #----------------------BOOK TESTS----------------------------

# book1 = create_book(title="Python 101", author_id= 1, published_year=2020, isbn="1234567890123")
# book2 = create_book(title="Python 102", author_id=1, published_year=2021, isbn="1234567890124")
# book3 = create_book(title="Python 103", author_id=1, published_year=2022, isbn=None)


# r = get_book_by_id(1)
# print(r)

# delete_book(1)
# print("AFTER DELETE BOOK:", get_book_by_id(1))

# r = get_all_books()
# print(r)

# search = search_books_by_title("Python")
# print(search)



# #---------------------STUDENT TESTS------------------------------

# student1 = create_student("Hasan", "hasan@mail.com")
# student2 = create_student("Husan", "husan@mail.com")

# student = get_student_by_id(2)
# print(student)

# update_student = update_student_grade(1, "1-kurs")
# print(update_student.grade, update_student)

# all_students = get_all_students()
# print(all_students)



# #---------------------BORROW TESTS------------------------------
# borrow1 = borrow_book(student_id=1, book_id=1)
# borrow2 = borrow_book(student_id=3, book_id=2)

# # Student1 kitob1 ni oladi
# borrow1 = borrow_book(student_id=1, book_id=1)
# print("Borrow1 record:", borrow1)


# borrow2 = borrow_book(student_id=3, book_id=2)
# print("Borrow2 record:", borrow2)


# borrow_fail = borrow_book(student_id=1, book_id=1)
# print("Borrow fail (should be None):", borrow_fail)


# Oldin 2 kitob oladi va 1 ta qoladi, shuni tekshirish mumkin

# borrow_book(student_id=1, book_id=2) 


# return_result1 = return_book(1)
# print(f"Return Borrow1 result (should be True): {return_result1}")


# return_fail = return_book(2)
# print(f"Return same borrow again (should be False): {return_fail}")


# return_result2 = return_book(1)
# print(f"Return Borrow2 result (should be True): {return_result2}")


# print(f"Book1 available: {get_book_by_id(1)}")
# print(f"Book2 available: {get_book_by_id(1)}")



# #-------------------------QUERY FUNKSIYALAR-----------------------------



# count_student1 = get_student_borrow_count(3)
# print(f"Talaba1 olgan kitoblar soni: {count_student1}")  

# count_student2 = get_student_borrow_count(1)
# print(f"Talaba2 olgan kitoblar soni: {count_student2}")  


# current_borrows = get_currently_borrowed_books()
# for book, student, borrowed_at in current_borrows:
#     print(f"{student.full_name} {book.title} kitobini {borrowed_at} da olgan")  


# author1 = create_author("Alisher Navoi", "G`azal mulkining sultoni")
# books_by_author1 = get_books_by_author(author1.id)
# for book in books_by_author1:
#     print(f"Muallif {author1.name} tomonidan yozilgan kitob: {book.title}")


# overdue_list = get_overdue_borrows()
# for borrow, student, book, days_late in overdue_list:
#     print(f"{student.full_name} {book.title} kitobini {days_late} kun kechiktirib qaytarmagan") 