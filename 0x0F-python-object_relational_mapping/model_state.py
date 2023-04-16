#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A State class that inherits from sqlalchemy declarative_base
    Attributes:
        Base (class)
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
