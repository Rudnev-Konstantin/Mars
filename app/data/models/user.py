from ..db import Declarative_Base
from sqlalchemy import Column, orm
from sqlalchemy import Integer, String, DateTime

import datetime


class User(Declarative_Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    
    age = Column(Integer, nullable=True)
    
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    
    address = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    
    modified_date = Column(DateTime, default=datetime.datetime.now)
    
    jobs = orm.relationship("Jobs", back_populates='user')
    
    def __repr__(self):
        return f"<Colonist> {self.id} {self.surname} {self.name}"
