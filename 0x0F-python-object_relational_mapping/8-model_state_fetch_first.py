#!/usr/bin/python3
"""This script will list the fisrt state in database"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).limit(1):
        print("{}: {}".format(state.id, state.name))
    if (session.query(State).count()) == 0:
        print("Nothing")
    session.close()
