from flask import Flask,  make_response, jsonify
from flask_cors import CORS
from datetime import datetime, timezone



# initialising the app
app = Flask(__name__)
CORS(app)

# defining the home route
@app.route('/', methods=['GET'])
def home():
    """
    This function returns a welcome message
    """
    return make_response(jsonify("Welcome to this api"))


# defining the api route
@app.route('/api', methods=['GET'])
def get_data():
    """
    This function return the basic information to the route
    """
    date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
              'email': 'godspel@gmail.com',
              'current_datetime': date,
              'github_url': 'https://github.com/GODSPE1/HNG-api'
            }

    return make_response(jsonify(data))


if __name__ == '__main__':
    app.run(debug=True)
