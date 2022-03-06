#!/usr/bin/python3
"""This file will create a class called State"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
if __name__ == "__main__":

    Base = declarative_base()

    class State(Base):
        """This is the class State with class attribute id and name"""
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement=True,
                    unique=True, nullable=False)
        name = Column(String(128), nullable=False)

        def __init__(self, name):
            """This initializes the given name"""
            self.name = name
