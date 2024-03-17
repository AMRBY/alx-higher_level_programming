#!/usr/bin/python3
"""
show all rows in a table
"""
from sqlalchemy.orm import Session
import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_mex = session.query(State).filter(State.id == 2).first()
    new_mex.name = 'New Mexico'
    session.add(new_mex)
    session.commit()
    session.close()
