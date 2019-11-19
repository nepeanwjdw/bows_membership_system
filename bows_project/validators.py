import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class FourDigitsValidator(object):
    def validate(self, pin, user=None):
        if not re.findall('\d{4}', pin):
            raise ValidationError(
                _("The pin must contain four digits, 0-9."),
                code='pin_not_four_digits',
            )

    def get_help_text(self):
        return _(
            "Your pin must contain four digits, 0-9."
        )
