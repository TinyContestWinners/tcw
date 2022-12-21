import datetime
import pytest
from sqlalchemy import text
from tcw.database import init_db, session


@pytest.fixture()
def db():
    init_db('sqlite://')


def test_contest_table(db):
    sql = text('SELECT * FROM contests')
    rows = session.execute(sql)
    assert len(rows.all()) == 0


def test_entrant_table(db):
    sql = text('SELECT * FROM entrants')
    rows = session.execute(sql)
    assert len(rows.all()) == 0
