from fastapi import APIRouter, Request, status, Response, Depends, HTTPException
from pydantic import BaseModel
import hashlib
from sqlalchemy.orm import Session
from db.db_connect import get_db
from utils.account import AccountService


router = APIRouter(prefix="/account")


class SignupRequest(BaseModel):
    email: str
    password: str


@router.post('/signup', tags=["Account"])
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    """ EP to sign up the user"""
    account_service = AccountService(db)

    if account_service.signup(request.email, request.password):
        return {
            'token': account_service.generate_token()
        }

    raise HTTPException(status_code=400, detail="Bad request")


@router.post('/login', tags=["Account"])
async def login(request: SignupRequest, db: Session = Depends(get_db)):
    """ EP to login the user"""
    account_service = AccountService(db)

    if account_service.login(request.email, request.password):
        return {
            'token': account_service.generate_token()
        }

    raise HTTPException(status_code=400, detail="Bad request")
