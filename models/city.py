#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="delete")
    
    else:
        state_id = ""
        name = ""