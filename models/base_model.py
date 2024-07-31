#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from os import getenv
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()
if not getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    
    id = Column(String(60), primary_key=True, nullable=False)
    format_str = '%Y-%m-%d %H:%M:%S.%f'
    created_at = Column(DateTime, nullable=False, default=(datetime.now()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.now()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            if (getenv('HBNB_TYPE_STORAGE') == 'file'):
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

            
        else:
            for key, value in kwargs.items():
                if getenv('HBNB_TYPE_STORAGE') == 'file':
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        if (getenv('HBNB_TYPE_STORAGE') == 'db'):
            self.id = str(uuid.uuid4())
        
        storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return dict representation of the instance with additional
        attributes and iso formatted date-time"""
        dict_rep = vars(self)
        dict_rep["__class__"] = self.__class__.__name__
        for key, value in dict_rep.copy().items():
            if key == "updated_at" or key == "created_at":
                dict_rep[key] = value.isoformat(timespec="microseconds")
            if key == '_sa_instance_state':
                del(dict_rep['_sa_instance_state'])
        return dict_rep
    
    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)