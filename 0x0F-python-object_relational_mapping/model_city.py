#!/usr/bin/python3
"""a Script that uses sqlalchemy to model our models using ORM
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    a Cities class that inherits from sqlalchemy declarative_base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
