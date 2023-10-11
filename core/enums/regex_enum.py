from enum import Enum


class RegEx(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,20}$',
        'First letter uppercase min 2 max 20 ch'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
