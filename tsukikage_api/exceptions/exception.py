"""Definition of exceptions."""


class BaseShirenError(Exception):
    """Base exception in this system."""


class BaseParameterError(BaseShirenError):
    """Base exception raised by invalid parameter."""


class BaseDBValueError(BaseShirenError):
    """Base exception raised when DB values are inconsistency."""


class PasswordUnmatchError(BaseParameterError):
    """Raised when password is unmatched with registered one."""


class TooLongAuthenticationParameterError(BaseParameterError):
    """Raised when authentication parameters are too long."""


class UserDuplicatedError(BaseDBValueError):
    """Raised when user record is duplicated."""
