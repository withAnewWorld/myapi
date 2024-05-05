from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)

question_voter = Table(
  'question_voter',
  Base.metadata,
  Column('user_id', Integer, ForeignKey('user.id'), primary_key = True),
  Column('question_id', Integer, ForeignKey('question.id'), primary_key = True)
)

answer_voter = Table(
  'answer_voter',
  Base.metadata,
  Column("user_id", Integer, ForeignKey("user.id"), primary_key = True),
  Column("answer_id", Integer, ForeignKey("answer.id"), primary_key = True),
)


class Question(Base):
  __tablename__ = "question"

  id = Column(Integer, primary_key = True)
  subject = Column(String, nullable = False)
  content = Column(Text, nullable=False)
  create_date = Column(DateTime, nullable = False)
  user_id = Column(Integer, ForeignKey("user.id"), nullable = True)
  user = relationship("User", backref = "question_users")
  modify_date = Column(DateTime, nullable = True)
  voter = relationship("User", secondary = question_voter, backref = 'question_voters')


class Answer(Base):
  __tablename__ = "answer"

  id = Column(Integer, primary_key = True)
  content = Column(Text, nullable = False)
  create_date = Column(DateTime, nullable = False)
  question_id = Column(Integer, ForeignKey("question.id"))
  question = relationship("Question", backref="answers")
  user_id = Column(Integer, ForeignKey("user.id"), nullable = True)
  user = relationship("User", backref = "answer_users")
  modify_date = Column(DateTime, nullable = True)
  voter = relationship("User", secondary = answer_voter, backref = "answer_voters")

class User(Base):
  __tablename__ = "user"

  id = Column(Integer, primary_key = True)
  username = Column(String, unique = True, nullable = False)
  password = Column(String, nullable=False)
  email = Column(String, unique=True, nullable=False)

