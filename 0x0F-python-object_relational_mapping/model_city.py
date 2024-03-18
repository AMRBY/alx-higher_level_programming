#!/usr/bin/python3
"""
this is ORM objects mapped to tables
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class mapped with cities table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
