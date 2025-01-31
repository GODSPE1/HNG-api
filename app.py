from flask import Flask,  make_response
from flask_cors import CORS
import datetime
import json


# initialising the app
app = Flask(__name__)
CORS(app)

# defining the route


@app.route('/', methods=['GET'])
def get_data():
    """
    This function return the basic information to the route
    """
    date = datetime.datetime.now(datetime.timezone.utc)
    data = {
              'email': 'godspel@gmail.com',
              'current_datetime': date.isoformat().replace("+00:00", "Z"),
              'github_url': 'https://github.com/GODSPE1/HNG-api'
            }

    return make_response(json.dumps(data))


if __name__ == '__main__':
    app.run(debug=True)
