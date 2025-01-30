from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from datetime import datetime
import json
date = datetime.now()

data = {
'email': 'godspelgmail.com',
'current_datetime': date.isoformat(),
'github_url': 'https://github.com/GODSPE1/HNG-api'
}

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_data():
        return make_response(json.dumps(data))
    

if __name__ == '__main__':
    app.run(debug=True)