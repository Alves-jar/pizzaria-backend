from fastapi import APIRouter, Depends, HTTPException
from models import User, db
from sqlalchemy.orm import sessionmaker
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    return {"message": "You've accessed the auth route.", "authenticated": False}

@auth_router.post("/create")
async def create(user_schema: UserSchema, session = Depends(get_session)):
    user = session.query(User).filter(User.email==user_schema.email).first()
    if user:
       raise HTTPException(status_code=400, detail="The provided email has been registered already")
    else:
        encrypted_password = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email, encrypted_password, user_schema.active, user_schema.admin)
        session.add(new_user)
        session.commit()
        return {"message": f"User registered successfully {user_schema.email}"}