from pydantic import BaseModel
from datetime import datetime


class UserSignupRequest(BaseModel):
    email: str
    password: str
    name: str


class UserDetailsResponse(BaseModel):
    email: str
    name: str
    created_at: datetime
    updated_at: datetime


class TokenRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
