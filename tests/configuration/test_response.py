"""Test response configuration."""
from unittest import TestCase

from tsukikage_api.configuration import ResponseConfig


class ResponseConfigTestCase(TestCase):
    """Action config test."""

    def test_value(self):
        """Test value."""
        response_config = ResponseConfig()

        assert response_config.response_start_tag != "foo"
        assert response_config.response_end_tag != "foo"
        assert response_config.response_ok != "foo"
        assert response_config.response_serial_error != "foo"
        assert response_config.response_auth_error != "foo"
        assert response_config.response_etc_error != "foo"
