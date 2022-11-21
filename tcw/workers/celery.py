import smtplib
from celery import Celery
from tcw.config import Development, Production
from tcw.database import session
from tcw.apps.contest.controllers import expired_contests
from .message import Message

# connect to flask environment
config = Development

# set up the celery app
app = Celery('tasks', broker=config.TCW_BROKER_URL)

@app.task
def handle_expired_contests():
    contests = expired_contests()
    for c in contests:
        finish_contest.delay(c.id)

@app.task
def finish_contest(contest_id):
    """
    Pick winners, notify owner, and delete the contest

    args:
        - int contest_id
    """

    try:
        contest = session.query(Contest).get(contest_id)
        winners = contest.pick_winners()
        notify_owner(contest, winners)
        session.delete(contest)
        session.commit()
    except:
        session.rollback()

def notify_owner(contest, winners):
    """
    Notify the contest owner of the winners

    args:
        - a Contest instance
        - a list of names
    """

    msg = Message(contest=contest, winners=winners).get_message()
    with smtplib.SMTP('localhost') as session:
        session.send_message(msg)

if __name__ == '__main__':
    app.start()
