import datetime
from sqlalchemy import text
from tcw.database import init_db, init_engine, engine, session


def test_init_all():
    assert init_db('sqlite://') is None


def test_init_engine():
    init_engine('sqlite://')
    assert session is not None


def test_contest_table():
    init_db('sqlite://')
    sql = text('SELECT * FROM contests')
    rows = session.execute(sql)
    assert len(rows.all()) == 0


def test_entrant_table():
    init_db('sqlite://')
    sql = text('SELECT * FROM entrants')
    rows = session.execute(sql)
    assert len(rows.all()) == 0


def test_insert():
    init_db('sqlite://')
    dt = datetime.datetime.utcnow()
    sql = text('''
        INSERT INTO contests (
            name,
            title,
            instructions,
            email,
            winners,
            max_entrants,
            expires)
        VALUES (
            "somerandomchars",
            "a test contest",
            "just add your username",
            "foo@bar.com",
            1,
            10,
            "%s"
        )''' % dt)
    session.execute(sql)
    session.commit()

    sql = text('SELECT * FROM contests')
    rows = session.execute(sql)
    assert len(rows.all()) == 1
