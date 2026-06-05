from fastapi import APIRouter
from models import User, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def home():
    return {"message": "You've accessed the auth route.", "authenticated": False}

@auth_router.post("/create")
async def create(name: str, email: str, password: str):
    Session = sessionmaker(bind=db)
    session = Session()
    user = session.query(User).filter(User.email==email).first()
    if user:
       return {"message": "The provided email has been registered already"} 
    else:
        new_user = User(name, email, password)
        session.add(new_user)
        session.commit()
        return {"message": "User registered successfully"}