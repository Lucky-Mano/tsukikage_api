"""Action configuration."""
from .base_config import BaseConfiguration


class ActionConfig(BaseConfiguration):
    """Action type config manager."""

    ACTION_CONF_PATH = "./config/action.json"

    def __init__(self) -> None:
        """Initialize."""
        super().__init__(self.ACTION_CONF_PATH)

    @property
    def register(self) -> str:
        """Return register value."""
        return self.config.get("register", "foo")

    @property
    def change(self) -> str:
        """Return change value."""
        return self.config.get("change", "foo")

    @property
    def authenticate(self) -> str:
        """Return auth value."""
        return self.config.get("authenticate", "foo")
