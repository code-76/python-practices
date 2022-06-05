from enum import Enum

class NumberSearchMode(Enum):
    LIST = 1
    SLOTS = 2

class NumberHitMode(Enum):
    Default = 1
    ODD = 2
    EVEN = 3
    ODD_AND_EVEN = 4
    VALIDATION = 5

class NumberTraceMode(Enum):
    HIT = 1
    ODD = 2
    EVEN = 3
    ODD_AND_EVEN = 4