"""Application main."""
from tsukikage_api.endpoint import api


def main():
    """Start application."""
    api.run(address="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
