from datetime import datetime, timedelta
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
    with get_db() as session:
        student = session.get(Student, student_id)
        book = session.get(Book, book_id)

        if not student:
            return None
        if not book:
            return None
        if book.is_available == False:
            return None

        # Talabada 3 tadan ortiq qaytarilmagan kitob yo`qmi shuni tekshirish uchun mana bunday logika qildim
        # buning logikasi shunday: avval borrowdagi student idsini olvolamiz va u oldin kirtob qaytargan yoki
        # qaytarmaganini bilish uchun 
        active_borrows = session.query(Borrow).filter(
            Borrow.student_id == student_id,
            Borrow.returned_at == None
        ).count()
        if active_borrows >= 3:
            return None

        borrowed_at = datetime.now()

        # datetime kutubxonasida timedelta degan method bor ekan, shu metoddan foydalanib qildim, yani aynan qaysiga kun, soat, yil qushmoqchi bulsak
        #shuni yozib vaqt kiritamiz masalan timedelta(hours=3)
        due_date = borrowed_at + timedelta(days=14)


        borrow = Borrow(
            student_id=student_id,
            book_id=book_id,
            borrowed_at=borrowed_at,
            due_date=due_date,
            returned_at=None
        )

        book.is_available = True  # kitobni band qilish
        book.is_available = False
        session.add(borrow)
        session.commit()
        
def return_book(borrow_id: int) -> bool:

    """
    Kitobni qaytarish
    
    Transaction ichida:
    - Borrow.returned_at ni to'ldirish
    - Book.is_available = True qilish
    
    Returns:
        True (muvaffaqiyatli) yoki False (xatolik)
    """
    with get_db() as session:
        borrow = session.get(Borrow, borrow_id)
        if not borrow:
            return False
        if borrow.returned_at != None:
            return False

        borrow.returned_at = datetime.now()

        book = session.get(Book, borrow.book_id)
        if book != None:
            book.is_available = True

        session.commit()
        
def get_student_borrow_count(student_id: int) -> int:
    """Talabaning jami olgan kitoblari soni"""
    with get_db() as session:
        count = session.query(Borrow).filter(Borrow.student_id == student_id).count()
        return count 
    
    
def get_currently_borrowed_books() -> list[tuple[Book, Student, datetime]]:
    """Hozirda band bo'lgan kitoblar va ularni olgan talabalar"""
    with get_db() as session:
        borrows = session.query(Borrow).filter(Borrow.returned_at == None).all()
        result = []
        for borrow in borrows:
            student = session.get(Student, borrow.student_id)
            book = session.get(Book, borrow.book_id)
            result.append((book, student, borrow.borrowed_at))
        return result 

def get_books_by_author(author_id: int) -> list[Book]:
    """Muayyan muallifning barcha kitoblari"""
    with get_db() as session:
        books = session.query(Book).filter(Book.author_id == author_id).all()
    return books

def get_overdue_borrows() -> list[tuple[Borrow, Student, Book, int]]:
    """
    Kechikkan kitoblar ro'yxati
    
    Returns:
        List of tuples: (Borrow, Student, Book, kechikkan_kunlar)
        faqat returned_at=NULL va due_date o'tgan yozuvlar
    """
    with get_db() as session:
        now = datetime.now()
        borrows = session.query(Borrow).filter(
            Borrow.returned_at == None,
            Borrow.due_date < now
        ).all()
        
        result = []
        for borrow in borrows:
            student = session.get(Student, borrow.student_id)
            book = session.get(Book, borrow.book_id)
            days_late = (now - borrow.due_date).days
            result.append((borrow, student, book, days_late))
        
        return result
            
