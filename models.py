from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType


db = create_engine("sqlite:///database.db")
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
        
        
class Order(Base):
    __tablename__ = "orders"
    
    ORDER_STATUS = (
    ("PENDING", "PENDING"),
    ("CANCELED", "CANCELED"),
    ("FINALIZED", "FINALIZED")
    )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=ORDER_STATUS))
    user = Column("user", ForeignKey("users.id"))
    price = Column("price", Float)
    # items =
    
    def __init__(self, user, status="PENDING", price=0):
        self.user = user
        self.status = status
        self.price = price
        
        
