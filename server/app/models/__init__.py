from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

association_table = Table('association', Base.metadata,
    Column('author_id', Integer, ForeignKey('author.id')),
    Column('book_id', Integer, ForeignKey('book.id'))
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    books = relationship("Book",
                    secondary=lambda: association_table,
                    backref="authors")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    authors = relationship("Author",
                    secondary=association_table)
