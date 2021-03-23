"""Test action configuration."""
from unittest import TestCase

from tsukikage_api.configuration import ActionConfig


class ActionConfigTestCase(TestCase):
    """Action config test."""

    def test_value(self):
        """Test value."""
        action_config = ActionConfig()

        assert action_config.register != "foo"
        assert action_config.change != "foo"
        assert action_config.authenticate != "foo"
