#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String, Float, Table, Integer, ForeignKey)
from sqlalchemy.orm import relationship
from os import getenv
import models

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    
    amenity_ids = []
    
    association_table = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60), ForeignKey("places.id"),
                                     primary_key=True, nullable=False),
                              Column("amenity_id", String(60), ForeignKey("amenities.id"),
                                     primary_key=True, nullable=False))


    
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            reviews_list= []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """
            """
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
