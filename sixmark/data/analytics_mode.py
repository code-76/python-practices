from enum import Enum

class NumberSearchMode(Enum):
    LIST = 1
    SLOTS = 2

class NumberAnalyticsMode(Enum):
    HIT = 1
    TYPE = 2
    TRACE = 3
    RANGE = 4