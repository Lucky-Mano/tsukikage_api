"""API endpoint is hear."""
import responder

api = responder.API(
    cors=True, cors_params={"allow_origins": ["*"], "allow_methods": ["GET", "POST"]}
)
