from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class UserCreate(BaseModel):
  username: str
  password1: str
  password2: str
  email: EmailStr

  @field_validator('username', 'password1', 'password2', 'email')
  def not_empty(cls, v):
    if not v or not v.strip():
      raise ValueError("null value is not allowed")
    return v
  
  @field_validator('password2')
  def passwords_match(cls, v, info: FieldValidationInfo):
    if 'password1' in info.data and v != info.data['password1']:
      raise ValueError("password isn't same")
    return v
  
class User(BaseModel):
  id: int
  username: str
  email: str

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str