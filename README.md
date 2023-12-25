# Flask-Status

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

The Flask Status Extension is a simple Flask extension that adds a status ping route to your Flask application. It allows you to easily check the health and status of your application or services by accessing a designated endpoint.

## Features

- **Status Endpoint**: Adds a status ping endpoint (`/api/status` by default) to your Flask application.
- **Custom Status Message**: Set a custom status message to provide more specific information about the health of your application.
- **Add more fields/data to status ping payload**: you can add more fields to the payload. This is helpful in cases where you want to add more info to the returned payload, for example, the state of the database.
- **Authenticated Ping route**: With `FlaskStatus`, you can now set the status ping route to be only accessed by authenticated users or requests.

See [below](#usage) for more info.

## Installation

To install the Flask Status Extension, you can use `pip`:

```bash
pip install flask-status
```

## Usage

Here's how to use the Flask-Status extension in your Flask application

- Install the package using pip

- create a file `main.py`

- Add the following to `main.py`

```python
from flask import Flask
from flask_status import FlaskStatus

app = Flask(__name__)
FlaskStatus(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

- run the `main.py` file

```bash
python3 main.py
```

- Now go to [http://localhost:5000/api/status](http://localhost:5000/api/status)

- You should see the following

```json
{
  "status": "OK"
}
```

You can also set the route for the status ping, and also the payload returned:

```python
app = Flask(__name__)
FlaskStatus(app, url="/api/ping", message={"message": "show my status"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

payload from [`http://localhost:5000/api/ping`](http://localhost:5000/api/ping):

```json
{
  "message": "show my status"
}
```

If the message is just a string and not a dictionary, example:

```python
FlaskStatus(app, message="Running")
```

It'd be converted to a JSON object payload by putting it in a `message` field as follows follows:

```json
{
  "message": "Running"
}
```

### Add more data

As said above, you can add more data to the status ping payload by using the `.add_field(key, value)` method. Example:

```python
flask_status = FlaskStatus(app)

flask_status.add_field("error", False)

# you can also add functions to run on request of the status route
def check_database():
    # check if database is running
    return True

flask_status.add_field("database", check_database)
```

The result payload of the above code is as follows:

```json
{
    "status": "OK",
    "error": false,
    "database": true
}
```

### Authenticate status route

You can now also set the status ping route to be for only authenticated users of the API by passing an `authenticator` function which should be a decorator function to the flask route function. Example:

```python
from functools import wraps

# define an authenticator decorator function
def login_required(self, func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get(AUTH_TOKEN_HEADER)
        if not token:
            return abort(401)
        if not verify_token(token):
            return abort(403)
        return func(*args, **kwargs)
  return wrapper

# define FlaskStatus with this authenticator function
FlaskStatus(app, authenticator=login_required)
```

The logic in the `authenticator` function would be run before returning the status payload in this manner:

```python
@app.route("/api/status")
@authenticator
def status_ping():
    return jsonify({"status": "OK"})
```

## Issues

If you encounter any issues with this extension or have suggestions for improvements, please create an issue on the [GitHub Issues page](https://github.com/Emmo00/flask-status/issues).

You are also welcome to contributing to this project.

Special thanks to the Flask community

## Author

- [Emmanuel Nwafor](https://github.com/Emmo00)

## Contributors

<a href="https://github.com/emmo00/flask-status/graphs/contributors">
	<p align="center">
  		<img src="https://contrib.rocks/image?repo=emmo00/flask-status" />
	</p>
</a>
