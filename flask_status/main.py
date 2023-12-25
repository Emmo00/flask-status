from types import FunctionType
from typing import Any, Dict, Callable
from flask import Flask, jsonify


class FlaskStatus:
    def __init__(
        self,
        app: Flask | None = None,
        url: str = "/api/status",
        message: str | Dict[str, str] = {"status": "OK"},
        authenticator: Callable[[Callable], Callable] = None,
    ):
        """Initialize flask-status"""
        if app is not None:
            self.init_app(app, url, message, authenticator)

    def init_app(
        self,
        app: Flask,
        url: str = "/api/status",
        message: str | Dict[str, str] = {"status": "OK"},
        authenticator: Callable[[Callable], Callable] = None,
    ) -> None:
        """Add flask app to flask-status"""
        if type(url) is not str:
            raise TypeError("Status Ping URL must be a string")
        if not url.startswith("/"):
            url = "/" + url
        self.status_ping_url = url

        if type(message) is str:
            self.status_message = {"message": message}
        elif type(message) is dict:
            self.status_message = message
        else:
            raise TypeError("Status Ping message must be a string or dictionary")

        if authenticator is not None:
            if type(authenticator) is not FunctionType:
                raise TypeError(
                    "Status Ping authenticator must be a decorator function"
                )

            @app.route(self.status_ping_url, methods=["GET"])
            @authenticator
            def status_ping():
                return jsonify(self.status_message), 200

            return

        @app.route(self.status_ping_url, methods=["GET"])
        def status_ping():
            return jsonify(self.status_message), 200

    def add_field(self, key: str, value: Any) -> None:
        """Add more field data to payload"""
        if type(key) is not str:
            raise TypeError("Status Ping field key must be a string")
        if type(value) is FunctionType:
            self.status_message[key] = value()
        else:
            try:
                import json

                json.dumps(value)
            except TypeError:
                raise TypeError("Status Ping field value is not JSON serializable")
            self.status_message[key] = value
