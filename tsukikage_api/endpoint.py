"""API endpoint is hear."""
import json
from logging import INFO, Formatter, getLogger
from pathlib import Path

import responder

log_level = INFO

logger = getLogger(__name__)
logger.setLevel(log_level)
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

api = responder.API(
    cors=True,
    cors_params={"allow_origins": ["*"], "allow_methods": ["GET", "POST"]},
)


@api.route("/api/auth")
def auth(req, resp):
    """Authenticate user."""
    response_path = Path("./config/response.json")
    with response_path.open() as fp:
        response_config = json.load(fp)
    resp.text = "\n".join(
        [
            response_config["response_start_tag"],
            response_config["response_ok"],
            response_config["response_end_tag"],
            "",
        ]
    )


@api.route("/api/rescue")
def rescue(req, resp):
    """Handle rescue request."""
    pass


@api.route("/api/ranking")
def ranking(req, resp):
    """Handle ranking request."""
    pass
