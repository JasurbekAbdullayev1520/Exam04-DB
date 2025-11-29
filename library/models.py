from datetime import datetime
from sqlalchemy import(
    Column, String, Boolean, Float, Integer, Date, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .db import Base, get_db



class Author(Base):
    __tablename__ = 'authors'

    author_id = Column('author_id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(length=64), nullable=False)
    bio = Column ('bio', String(length=256))

    book = relationship('Book', back_populates='author')

    def __str__(self):
        return f'Author (id= {self.author_id}, Name= ( {self.name}))'
    
    def __repr__(self):
        return f'author (id= {self.author_id}, Name= ( {self.name}))'
    

class Book(Base):
    __tablename__ = 'book'
    id = Column('id', Integer, primary_key=True, nullable=False)
    author_id = Column('author_id', ForeignKey('authors.author_id', ondelete='CASCADE'))
    title = Column('title', String(length=200), nullable=False)
    published_year = Column('published_year', Integer)
    isbn = Column('isbn', String(length=13), unique=True, nullable=False)
    is_available = Column('is_available', Boolean, default=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
    
    author = relationship('Author', back_populates='book')
    borrows = relationship('Borrow', back_populates='book')



    def __str__(self):
        return f"Book(title={self.title}, author_id={self.author_id})"

    
    def __repr__(self):
        return f"<Book id={self.id}, title='{self.title}', author_id={self.author_id}>"
    
    
class Student(Base):
    __tablename__ = 'students'
    
    id = Column('id', Integer, primary_key=True, nullable=False)
    full_name = Column('full_name', String(length=64), nullable=False)
    email = Column('email', String(length=100), nullable=False)
    grade = Column('grade', String(length=20))
    registered_at = Column('registered_at', DateTime, default=datetime.now)
    
    borrow = relationship('Borrow', back_populates='student')

    
    def __str__(self):
        return f"Student(full_name={self.full_name}, Borrow id={self.id})"

    
    def __repr__(self):
        return f"<Student id={self.id}, full_name='{self.full_name}', Borrow id={self.id}>"
    
    
class Borrow(Base):
    __tablename__ = 'borrows'
    
    id = Column('id', Integer, primary_key=True, nullable=False)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    book_id = Column('book_id', ForeignKey('book.id', ondelete='CASCADE'))
    borrowed_at = Column('borrowed_at', DateTime, default=datetime.now)
    due_date = Column('due_date', DateTime, default=datetime.now)
    returned_at = Column('returned_at', DateTime, default=datetime.now, onupdate=datetime.now)
    
    student = relationship('Student', back_populates='borrow')

    book = relationship('Book', back_populates='borrows')