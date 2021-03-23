"""Test parameter configuration."""
from unittest import TestCase

from tsukikage_api.configuration import ParameterConfig


class ParameterConfigTestCase(TestCase):
    """Action config test."""

    def test_value(self):
        """Test value."""
        param_config = ParameterConfig()

        assert param_config.name != "foo"
        assert param_config.password != "foo"
        assert param_config.serial != "foo"
        assert param_config.action != "foo"
        assert param_config.old_password != "foo"
        assert param_config.new_password != "foo"
