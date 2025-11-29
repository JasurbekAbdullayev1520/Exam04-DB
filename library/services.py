from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Author, Book, Student, Borrow
from .db import get_db

# Author CRUD
def create_author(name: str, bio: str = None) -> Author:
    author = Author(
        name = name,
        bio = bio
        
    )
    with get_db() as session:
        session.add(author)
        session.commit()

def get_author_by_id(author_id: int) -> Author | None:
    """ID bo'yicha muallifni olish"""
    with get_db() as session:
        author = session.query(Author).get(author_id)

    return author


def get_all_authors() -> list[Author]:
    """Barcha mualliflar ro'yxatini olish"""
    with get_db() as session:
        author = session.query(Author).all()

    return author

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    author_id: int | None = None,
    name: str | None = None,  
    bio: str | None = None,
    
    author = get_author_by_id(author_id)

    if author:
        with get_db() as session:
            author.name = name if name else author.name
            author.bio = bio if bio else author.bio

            session.add(author)
            session.commit()

def delete_author(author_id: int) -> bool:
    """Muallifni o'chirish (faqat kitoblari bo'lmagan holda)"""
    author = get_author_by_id(author_id)

    if author:
        with get_db() as session:
            session.delete(author)
            session.commit()
            
#Book CRUD 
def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    """Yangi kitob yaratish"""
    book = Book(
        title = title,
        author_id = author_id,
        published_year = published_year,
        isbn = isbn
        
    )
    with get_db() as session:
        session.add(book)
        session.commit()

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    with get_db() as session:
        book = session.query(Book).get(book_id)

    return book

def get_all_books() -> list[Book]:
    """Barcha kitoblar ro'yxatini olish"""
    with get_db() as session:
        book = session.query(Book).all()

    return book

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni sarlavha bo'yicha qidirish (partial match)"""
    with get_db() as session:
        books = session.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
        return books

def delete_book(book_id: int) -> bool:
    """Kitobni o'chirish"""
    book = get_book_by_id(book_id)

    if book:
        with get_db() as session:
            session.delete(book)
            session.commit()
            
#Student CRUD
def create_student(full_name: str, email: str, grade: str = None) -> Student:
    """Yangi talaba ro'yxatdan o'tkazish"""
    student = Student(
        full_name = full_name,
        email = email,
        grade = grade,
    )
    with get_db() as session:
        session.add(student)
        session.commit()

def get_student_by_id(student_id: int) -> Student | None:
    """ID bo'yicha talabani olish"""
    with get_db() as session:
        student = session.query(Author).get(student_id)

    return student

def get_all_students() -> list[Student]:
    """Barcha talabalar ro'yxatini olish"""
    with get_db() as session:
        student = session.query(Student).all()

    return student

def update_student_grade(student_id: int, grade: str) -> Student | None:
    """Talaba sinfini yangilash"""
    student_id: int | None = None,
    grade: str | None = None,
    
    student = get_student_by_id(student_id)

    if student:
        with get_db() as session:
            student.grade = grade if grade else student.grade

            session.add(student)
            session.commit()
            
def delete_student(student_id: int) -> bool:
    """Studentni o'chirish"""
    student = get_student_by_id(student_id)

    if student:
        with get_db() as session:
            session.delete(student)
            session.commit()
            
# Borrow/Return Logic
def borrow_book(student_id: int, book_id: int) -> Borrow | None:
    """
    Talabaga kitob berish
    
    Quyidagilarni tekshirish kerak:
    1. Student va Book mavjudligini
    2. Kitobning is_available=True ekanligini
    3. Talabada 3 tadan ortiq qaytarilmagan kitob yo'qligini yani 3 tagacha kitob borrow qila oladi
    
    Transaction ichida:
    - Borrow yozuvi yaratish
    - Book.is_available = False qilish
    - due_date ni hisoblash (14 kun)
    
    Returns:
        Borrow object yoki None (xatolik bo'lsa)
    """
    pass

            
