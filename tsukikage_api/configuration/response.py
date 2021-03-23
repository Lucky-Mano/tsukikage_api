"""Response configuration."""
from .base_config import BaseConfiguration


class ResponseConfig(BaseConfiguration):
    """Response config."""

    RESPONSE_CONF_PATH = "./config/response.json"

    def __init__(self) -> None:
        """Initialize."""
        super().__init__(self.RESPONSE_CONF_PATH)

    @property
    def response_start_tag(self) -> str:
        """Return response_start_tag value."""
        return self.config.get("response_start_tag", "foo")

    @property
    def response_end_tag(self) -> str:
        """Return response_end_tag value."""
        return self.config.get("response_end_tag", "foo")

    @property
    def response_ok(self) -> str:
        """Return response_ok value."""
        return self.config.get("response_ok", "foo")

    @property
    def response_serial_error(self) -> str:
        """Return response_serial_error value."""
        return self.config.get("response_serial_error", "foo")

    @property
    def response_auth_error(self) -> str:
        """Return response_auth_error value."""
        return self.config.get("response_auth_error", "foo")

    @property
    def response_etc_error(self) -> str:
        """Return response_etc_error value."""
        return self.config.get("response_etc_error", "foo")
