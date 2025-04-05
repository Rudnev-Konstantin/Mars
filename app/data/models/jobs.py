from ..db import Declarative_Base
from flask_login import UserMixin
from sqlalchemy import Column, orm
from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey

import datetime


class Jobs(Declarative_Base, UserMixin):
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey("users.id"))
    
    job = Column(String, nullable=True)
    
    work_size = Column(Integer, nullable=True)
    
    collaborators = Column(String, nullable=True)
    
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime, nullable=True)
    
    is_finished = Column(Boolean, default=False)
    
    user = orm.relationship('User')
