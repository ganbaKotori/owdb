from dataclasses import dataclass
from sqlalchemy import Enum
from app import db
import enum

class MatchPhase(enum.Enum):
    ATTACK = "ATTACK"
    DEFEND = "DEFEND"

    def __str__(self):
        return self.value