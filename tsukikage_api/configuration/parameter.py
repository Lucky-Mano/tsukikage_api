"""Parameter configuration."""
from .base_config import BaseConfiguration


class ParameterConfig(BaseConfiguration):
    """Parameter config."""

    PARAMETER_CONF_PATH = "./config/parameters.json"

    def __init__(self) -> None:
        """Initialize."""
        super().__init__(self.PARAMETER_CONF_PATH)

    @property
    def name(self) -> str:
        """Return name value."""
        return self.config.get("name", "foo")

    @property
    def password(self) -> str:
        """Return password value."""
        return self.config.get("password", "foo")

    @property
    def serial(self) -> str:
        """Return serial value."""
        return self.config.get("serial", "foo")

    @property
    def action(self) -> str:
        """Return action value."""
        return self.config.get("action", "foo")

    @property
    def old_password(self) -> str:
        """Return old password value."""
        return self.config.get("old_password", "foo")

    @property
    def new_password(self) -> str:
        """Return new password value."""
        return self.config.get("new_password", "foo")
