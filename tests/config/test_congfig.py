"""Config tests."""
import json
from pathlib import Path
from unittest import TestCase


class ConfigTestCase(TestCase):
    """All configs test."""

    def test_action_config(self):
        """Test action config."""
        action_path = Path("./config/action.json")
        assert action_path.exists()

        with action_path.open() as fp:
            conf = json.load(fp)

        assert "register" in conf
        assert "change" in conf
        assert "authenticate" in conf

    def test_parameters_config(self):
        """Test parameters config."""
        params_path = Path("./config/parameters.json")
        assert params_path.exists()

        with params_path.open() as fp:
            conf = json.load(fp)

        assert "name" in conf
        assert "password" in conf
        assert "serial" in conf
        assert "action" in conf
        assert "old_password" in conf
        assert "new_password" in conf

    def test_response_config(self):
        """Test response config."""
        response_path = Path("./config/response.json")
        assert response_path.exists()

        with response_path.open() as fp:
            conf = json.load(fp)

        assert "response_start_tag" in conf
        assert "response_end_tag" in conf
        assert "response_ok" in conf
        assert "response_serial_error" in conf
        assert "response_auth_error" in conf
        assert "response_etc_error" in conf
