"""Application main."""
from logging import INFO, Formatter, getLogger
from logging.handlers import RotatingFileHandler

log_level = INFO

logger = getLogger(__name__)
logger.setLevel(log_level)
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = RotatingFileHandler(filename="/var/log/tsuki/api.log", maxBytes=8192, backupCount=5)

file_handler.setLevel(log_level)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
    """Start application."""
    pass


if __name__ == "__main__":
    main()
