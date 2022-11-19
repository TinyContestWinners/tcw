import argparse
import smtplib
from email.message import EmailMessage
from tcw.config import Development, Production
from tcw.database import session, init_db
from tcw.apps.contest.controllers import expired_contests
from tcw.apps.contest.models import Contest, Entrant
from tcw.message import TCWMessage

# globals #
args = None


def main():
    parse_args()
    if args.environment == 'development':
        config = Development
    else:
        config = Production

    init_db(config.SQLALCHEMY_DATABASE_URI, config.DEBUG)
    finish_contests(config)


def parse_args():
    global args
    parser = argparse.ArgumentParser(description='Process Tiny Contest Winners jobs.')
    parser.set_defaults(environment='production')
    parser.add_argument('--development', action='store_const',
                    const='development', dest='environment',
                    help='specify development environment')

    args = parser.parse_args()


def finish_contests(config):
    try:
        contests = expired_contests()
        if not contests:
            return
    except Exception as x:
        print(x)
        return

    for c in contests:
        try:
            c.pick_winners()
            notify_owner(c)
            c.email = ''
            remove_entrants(c.id)
            session.commit()
        except:
            session.rollback()


def remove_entrants(contest_id):
    session.query(Entrant).filter(Entrant.contest_id == contest_id).delete()


def notify_owner(contest):
    msg = TCWMessage(contest=contest).get_message()
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)


if __name__ == '__main__':
    main()
