import datetime
from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User


class Question(BaseModel):
  id: int
  subject: str
  content: str
  create_date: datetime.datetime
  answers: list[Answer] = []
  user: User | None
  modify_date: datetime.datetime | None = None
  voter: list[User] = []

class QuestionList(BaseModel):
  total: int = 0
  question_list: list[Question] = []

class QuestionCreate(BaseModel):
  subject: str
  content: str

  @field_validator('subject', 'content')
  def not_empy(cls, v):
    if not v or not v.strip():
      raise ValueError("null value is not allowed")
    return v
  
class QuestionUpdate(QuestionCreate):
  question_id: int

class QuestionDelete(BaseModel):
  question_id: int

class QuestionVote(BaseModel):
  question_id: int