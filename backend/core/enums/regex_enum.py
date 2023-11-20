from enum import Enum

from django.utils.translation import gettext_lazy as _


class RegEx(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,20}$',
        'First letter uppercase min 2 max 20 ch'
    )
    AUTO_PARK_NAME = (
        r'^[A-Z][a-zA-Z]{1,20}$',
        'Only letters and first uppercase min 2 max 20 ch'
    )

    NAME = (
        r'^[А-ЯЁІЇЄҐ][а-яіїєґё]{1,49}$',
        [
            _('Only cyrillic'),
            _('First letter uppercase'),
            _('min 2 max 50 characters')
        ]
    )

    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*\d)'
        r'(?=.*[`~!@#$%^&*()_\-+=\\|\[\]{};:\'"\/\?\.>,<])[a-zA-Z\d`~!@#$%^&*()_\-+=\\|\[\]{};:\'"\/\?\.>,<]{8,30}$',
        [
            'min 1 lowercase',
            'min 1 uppercase',
            'min 1 digit',
            'min 1 special character',
            'length 8-30 ch'
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
