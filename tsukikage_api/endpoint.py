"""API endpoint is hear."""
import json
from logging import getLogger
from pathlib import Path

import responder

logger = getLogger(__name__)

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
