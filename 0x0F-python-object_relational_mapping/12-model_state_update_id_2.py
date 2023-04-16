#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, data))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = session.query(State).filter(State.id == 2).one()
    new_state.name = "New Mexico"
    session.commit()
