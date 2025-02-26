from datetime import timedelta
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .auth import (
    authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, get_password_hash
)
from .model import UserSignupRequest, TokenRequest, TokenResponse, UserDetailsResponse

from backend.database.tools import create_user
from backend.database.db import get_db
from backend.database.models import User


router = APIRouter()


@router.post("/token", response_model=TokenResponse)
async def login_for_access_token(token_request: TokenRequest, db: Session = Depends(get_db)) -> Dict[str, str]:
    # Authenticate the user using the provided email and password.
    user = authenticate_user(db, token_request.email, token_request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    # Create the JWT token without any client id/secret
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id, "type": "user"},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(
    current_user: User = Depends(get_current_user)
):
    """Get details of currently authenticated user"""
    return UserDetailsResponse(
        email=current_user.email,
        name=current_user.name,
        created_at=current_user.created_at,
        updated_at=current_user.updated_at
    )


@router.post("/register")
async def register(
    user_details: UserSignupRequest,
    db: Session = Depends(get_db)
):
    """User registration endpoint for password flow"""
    try:
        hashed_password = get_password_hash(user_details.password)
        user = create_user(db=db, email=user_details.email, password=hashed_password, name=user_details.name)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    