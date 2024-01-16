#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column( String(128), nullable=False)
    
    city = relationship('City', backref='state',cascade="all, delete, delete-orphan")