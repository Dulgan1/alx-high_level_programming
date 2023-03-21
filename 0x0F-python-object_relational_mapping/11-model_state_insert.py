#!/usr/bin/python3

"""
    Script creates new instance of State in database
    argv[1] -> user to access db
    argv[2] -> password to access db
    argv[3] -> Database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    eng_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                               argv[2],
                                                               argv[3])
    engine = create_engine(eng_str, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    print("{:d}".format(new_state.id))

    session.close()
