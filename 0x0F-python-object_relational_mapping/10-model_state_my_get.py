#!/usr/bin/python3

"""
Script  displays State instances with the passed argv[4] as name
in a database
    argv[1] -> user to access db
    argv[2] -> password to access db
    argv[3] -> Database (db)
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

if __name__ == "__main__":
    eng_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                               argv[2],
                                                               argv[3])
    engine = create_engine(eng_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(Stae).filter_by(name=argv[4]).order_by(State.id)

    if instance:
        print("{:d}".format(instance.id))
    else:
        print("Not found")

    session.close()
