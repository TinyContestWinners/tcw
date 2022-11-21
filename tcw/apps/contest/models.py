import datetime
import secrets
from sqlalchemy import (Column, Integer, Unicode, UnicodeText, DateTime,
    Boolean, ForeignKey, func)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint
from tcw.database import Base
from tcw.models.ext import MutableDict, JSONEncodedDict

class Contest(Base):
    __tablename__ = 'contests'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(48), nullable=False, unique=True)
    title = Column(Unicode(128), nullable=False)
    instructions = Column(UnicodeText, nullable=True)
    email = Column(Unicode(128), nullable=True)
    expires = Column(DateTime, nullable=False, default=func.now())
    winners = Column(Integer, nullable=False, default=1)
    max_entrants = Column(Integer, nullable=False, default=100)
    attributes = Column(MutableDict.as_mutable(JSONEncodedDict), nullable=True)

    # relationships
    entrants = relationship('Entrant', backref='contest', cascade='all,delete')


    def pick_winners(self):
        """
        Pick the winners of the contest.

        args:
            None
        returns:
            list - a list of winning names
        """

        results = []

        # not enough entrants? re-adjust winner size
        if len(self.entrants) < self.winners:
            self.winners = len(self.entrants)

        choices = [e.name for e in self.entrants]
        while len(results) < self.winners:
            name = secrets.choice(choices)
            if name not in results:
                results.append(name)

        return results


class Entrant(Base):
    __tablename__ = 'entrants'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False, unique=False)
    contest_id = Column(Integer, ForeignKey('contests.id'))

    # ensure only one name sign-up per contest.
    __table_args__ = (
        UniqueConstraint('name', 'contest_id', name='_name_id_uc'),)
