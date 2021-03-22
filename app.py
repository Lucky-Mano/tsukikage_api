"""Application main."""
from logging import INFO, Formatter, getLogger

from tsukikage_api.endpoint import api

log_level = INFO

logger = getLogger(__name__)
logger.setLevel(log_level)
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def main():
    """Start application."""
    api.run(address="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
