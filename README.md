# Flask-Status

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

The Flask Status Extension is a simple Flask extension that adds a status ping route to your Flask application. It allows you to easily check the health and status of your application or services by accessing a designated endpoint.

## Features

- **Status Endpoint**: Adds a `/api/status` endpoint to your Flask application.
- **Custom Status Message**(coming soon): Set a custom status message to provide more specific information about the health of your application.
- **Logging**(coming soon): Logs incoming requests to the status endpoint and changes to the custom status message for monitoring purposes.

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
FlaskStatus(app, url="/api/status", message={"message": "show my status"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
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

If custom message is passed, then:

```json
{
  "message": "show my status"
}
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
