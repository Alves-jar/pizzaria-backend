from fastapi import APIRouter, Depends
from models import User, db
from sqlalchemy.orm import sessionmaker
from dependencies import get_session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    return {"message": "You've accessed the auth route.", "authenticated": False}

@auth_router.post("/create")
async def create(name: str, email: str, password: str, session = Depends(get_session)):
    user = session.query(User).filter(User.email==email).first()
    if user:
       return {"message": "The provided email has been registered already"} 
    else:
        encrypted_password = bcrypt_context.hash(password)
        new_user = User(name, email, encrypted_password)
        session.add(new_user)
        session.commit()
        return {"message": "User registered successfully"}