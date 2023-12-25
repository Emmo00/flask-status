from typing import Any
from flask import Flask, jsonify


class FlaskStatus:
    def __init__(
        self,
        app: Flask | None = None,
        url: str = "/api/status",
        message: Any = {"status": "OK"},
    ):
        self.status_ping_url = url
        self.status_message = message
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        @app.route(self.status_ping_url, methods=["GET"])
        def status_ping():
            return jsonify(self.status_message), 200
