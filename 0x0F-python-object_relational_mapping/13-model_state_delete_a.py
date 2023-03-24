#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name 
                containing the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments:
                    mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
                            from model_state import Base, State
Your script should connect to a MySQL server 
                                running on localhost at port 3306
Your code should not be executed when imported
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    states = session.query(State).filter(State.name.like('%a%')).all()
    for s in states:
        session.delete(s)

    session.commit()
    session.close()
