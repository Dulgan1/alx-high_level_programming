#!/usr/bin/python3

"""
    Script displays all State objects that begin with 'a'
    in a database
    argv[1] -> user to acess db
    argv[2] -> password to access db
    argv[3] -> database (db)
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng_str = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                          argv[2],
                                                          argv[3])
    engine = create_engine(eng_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))

    session.close()
