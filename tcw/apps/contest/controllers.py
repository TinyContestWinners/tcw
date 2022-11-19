import datetime
from sqlalchemy import func, or_, and_
from tcw.database import session
from .models import Contest, Entrant


def contest_by_name(name):
    contest = session.query(Contest).filter(Contest.name == name).one()
    if not contest:
        raise Exception("No contest with name %s" % name)

    return contest


def expired_contests():
    now = datetime.datetime.utcnow()
    subq = session.query(
        func.count(Contest.entrants) >= Contest.max_entrants).scalar_subquery()

    contests = session.query(Contest).filter(
        or_(
            (and_( Contest.final == None, Contest.expires < now )),
            (and_( Contest.final == None, subq ))
        )
    ).all()

    if not contests:
        raise Exception("No contests that meet criteria")

    return contests
