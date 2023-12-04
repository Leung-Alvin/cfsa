from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, Enum
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import enum

# Connect to the SQLite database (Creates if doesn't exist)
engine = create_engine('sqlite:///csfa.db', echo=True)

# Create a base class for declarative models
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    name = Column(String)

    # One-to-Many relationship: One Author can have multiple Corpora
    corpora = relationship("Corpus", backref="author")

class CorpusType(enum.Enum):
    other = 'other'
    formal = 'formal'
    informal = 'informal'
    survey = 'survey'

class Corpus(Base):
    __tablename__ = 'corpora'

    corpus_id = Column(Integer, primary_key=True)
    corpus_type = Column(Enum(CorpusType))
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    title = Column(String)
    text_content = Column(Text)

class Question(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer, primary_key=True)
    text = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

"""
# Migration Code
import os
import glob

def add_author(name):
    author = session.query(Author).filter_by(name=name).first()
    if not author:
        author = Author(name=name)
        session.add(author)
        session.commit()
    return author

def add_corpus(author, title, corpus_type, text_content):
    corpus = Corpus(title=title, corpus_type=corpus_type, text_content=text_content, author_id=author.author_id)
    session.add(corpus)
    session.commit()

def add_question(text):
    question = Question(text=text)
    session.add(question)
    session.commit()

# Importing Corpus Data
for corpus_type in CorpusType:
    path = f"databases/{corpus_type.value}/*"
    for file_path in glob.glob(path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        _, tail = os.path.split(file_path)
        author_name, title = tail.split('_-_')
        title = title[:-4]  # Remove '.txt'
        author = add_author(author_name)
        add_corpus(author, title, corpus_type, text_content)

# Importing Question Data
with open('prompts.txt', 'r', encoding='utf-8') as file:
    questions = file.readlines()
    for question in questions:
        question_text = question.strip('- "\n')
        add_question(question_text)
"""

session.close()