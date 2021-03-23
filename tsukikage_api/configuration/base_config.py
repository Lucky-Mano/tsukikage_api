"""Base configuration."""
import json
from abc import ABC
from pathlib import Path
from typing import Dict


class BaseConfiguration(ABC):
    """Base configuration class."""

    def __init__(self, path: str) -> None:
        """Initialize.

        Args:
            path: config file path.

        """
        conf_path = Path(path)
        with conf_path.open() as fp:
            self.config: Dict = json.load(fp)
