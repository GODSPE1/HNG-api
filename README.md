# HNG SIMPLE API
 https://hng.tech/hire/python-developers

## Project Description
* This project is a simple API to display basic information
* It is really simple to set up and to follow through.

## Tech Stack
- Python with flask
- deployed on https://hng-api-1.onrender.com/api


## HOW TO SET UP
- Ensure you have: 
python insatlled,
Git

1. Clone the repo. 
git clone `https://github.com/GODSPE1/HNG-api.git`
cd your-repo

2. Install Dependencies.

Install all the dependencies using the reqiurements.txt

pip install requirements.txt

3. Start the server, to run the api locally.

- Next run the command `flask run` or ` python3 app.py` to start the server


4. Test the API
Once the server is running, open your browser or use Postman/cURL to send a GET request to:
http://localhost:5000

### Response Format (`200 OK`)
```json
{
    "email":"godspe18@gmail.com",
"current_datetime":"2025-01-30T19:16:16.198Z",
"github_url":"https://github.com/GODSPE1/HNG-api.git"
}


And That is all you need to visualize the simple API :).