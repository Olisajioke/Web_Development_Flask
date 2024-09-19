import math
from wtforms import ValidationError
from email_validator import validate_email, EmailNotValidError


class NumberRange:
    """
    Validates that a number is of a minimum and/or maximum value, inclusive.
    This will work with any comparable number type, such as floats and
    decimals, not just integers.

    :param min:
        The minimum required value of the number. If not provided, minimum
        value will not be checked.
    :param max:
        The maximum value of the number. If not provided, maximum value
        will not be checked.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated using `%(min)s` and `%(max)s` if desired. Useful defaults
        are provided depending on the existence of min and max.

    When supported, sets the `min` and `max` attributes on widgets.
    """

    def __init__(self, min=None, max=None, message=None):
        self.min = min
        self.max = max
        self.message = message
        self.field_flags = {}
        if self.min is not None:
            self.field_flags["min"] = self.min
        if self.max is not None:
            self.field_flags["max"] = self.max

    def __call__(self, form, field):
        data = field.data
        if (
            data is not None
            and not math.isnan(data)
            and (self.min is None or data >= self.min)
            and (self.max is None or data <= self.max)
        ):
            return

        if self.message is not None:
            message = self.message

        # we use %(min)s interpolation to support floats, None, and
        # Decimals without throwing a formatting exception.
        elif self.max is None:
            message = field.gettext("Number must be at least %(min)s.")

        elif self.min is None:
            message = field.gettext("Number must be at most %(max)s.")

        else:
            message = field.gettext("Number must be between %(min)s and %(max)s.")

        raise ValidationError(message % dict(min=self.min, max=self.max))
    



class LengthRange:
    """
    Validates that the length of a string is within a minimum and/or maximum value, inclusive.

    :param min:
        The minimum required length of the string. If not provided, minimum
        length will not be checked.
    :param max:
        The maximum length of the string. If not provided, maximum length
        will not be checked.
    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated using `%(min)s` and `%(max)s` if desired. Useful defaults
        are provided depending on the existence of min and max.
    """

    def __init__(self, min=None, max=None, message=None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form, field):
        length = len(field.data)
        if (
            (self.min is None or length >= self.min)
            and (self.max is None or length <= self.max)
        ):
            return

        if self.message is not None:
            message = self.message
        elif self.max is None:
            message = field.gettext("Field must be at least %(min)d characters long.")
        elif self.min is None:
            message = field.gettext("Field must be at most %(max)d characters long.")
        else:
            message = field.gettext("Field must be between %(min)d and %(max)d characters long.")

        raise ValidationError(message % dict(min=self.min, max=self.max))





class Email:
    """
    Validates an email address. Requires email_validator package to be
    installed. For ex: pip install wtforms[email].

    :param message:
        Error message to raise in case of a validation error.
    :param granular_message:
        Use validation failed message from email_validator library
        (Default False).
    :param check_deliverability:
        Perform domain name resolution check (Default False).
    :param allow_smtputf8:
        Fail validation for addresses that would require SMTPUTF8
        (Default True).
    :param allow_empty_local:
        Allow an empty local part (i.e. @example.com), e.g. for validating
        Postfix aliases (Default False).
    """

    def __init__(
        self,
        message=None,
        granular_message=False,
        check_deliverability=False,
        allow_smtputf8=True,
        allow_empty_local=False,
    ):
        self.message = message
        self.granular_message = granular_message
        self.check_deliverability = check_deliverability
        self.allow_smtputf8 = allow_smtputf8
        self.allow_empty_local = allow_empty_local

    def __call__(self, form, field):
        try:
            if field.data is None:
                raise EmailNotValidError()
            validate_email(
                field.data,
                check_deliverability=self.check_deliverability,
                allow_smtputf8=self.allow_smtputf8,
                allow_empty_local=self.allow_empty_local,
            )
        except EmailNotValidError as e:
            message = self.message
            if message is None:
                if self.granular_message:
                    message = str(e)
                else:
                    message = field.gettext("Invalid email address.")
            raise ValidationError(message) from e
