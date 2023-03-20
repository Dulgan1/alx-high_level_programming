#!/usr/bin/python3

"""
    Script disolays first State object from a database
    argv[1] -> user to access db
    argv[2] -> password to access db
    argv[3] -> database db
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(eng_str.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).order_by(State.id).first()
    if instance:
        print("{:d}: {:s}".format(instance.id, instance.name))
    else:
        print("Nothing")

    session.close()
