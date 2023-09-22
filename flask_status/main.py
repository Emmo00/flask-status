from flask import Flask, jsonify


class FlaskStatus:
    def __init__(self, app: Flask | None = None, url="/api/status"):
        self.status_ping_url = url
        if app is not None:
            self.init_app()

    def init_app(self, app: Flask):
        @app.route(self.status_ping_url, methods=["GET"])
        def status_ping():
            return jsonify({"status": "OK"}), 200
