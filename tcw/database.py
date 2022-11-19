from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base

# globals #
engine = None
session = scoped_session(lambda: create_session( bind=engine,
                                                    autocommit=False,
                                                    autoflush=False ))

Base = declarative_base()
Base.query = session.query_property()

def init_db(uri, echo=False):
    init_engine(uri, echo=echo)
    init_tables()


def init_engine(uri, *args, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)


def init_tables():
    from tcw.apps.contest.models import Contest, Entrant
    Base.metadata.create_all(bind=engine)
