#!/usr/bin/python3
"""This script will print the id of the user inputed State"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import text

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    St = sys.argv[4]
    for state in session.query(State).filter(text("name = :name"))\
                                     .params(name=St):
        print("{}" .format(state.id))
    if ((session.query(State).filter(text("name=:name"))
                             .params(name=St).count()) == 0):
        print("Not found")
    session.close()
