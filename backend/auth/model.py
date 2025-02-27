from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserInformation(BaseModel):
    age_range: str
    habit_struggle: str
    wellness_goals: List[str]
    sleep_quality: str
    stress_level: str
    check_in_style: str


class UserSignupRequest(BaseModel):
    email: str
    password: str
    name: str
    information: UserInformation


class UserSignupResponse(BaseModel):
    email: str
    name: str
    information: UserInformation
    created_at: datetime
    updated_at: datetime


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
