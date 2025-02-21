from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# User details (hardcoded for demonstration)
user_details = {
    "user_id": "john_doe_17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123"
}

# POST method endpoint
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    
    # Separate numbers and alphabets
    numbers = [item for item in data if str(item).isdigit()]
    alphabets = [item for item in data if isinstance(item, str) and len(item) == 1 and item.isalpha()]

    # Determine the highest alphabet (case insensitive)
    highest_alphabet = []
    if alphabets:
        max_alphabet = max(alphabets, key=lambda x: x.upper())
        highest_alphabet = [max_alphabet]  # Wrap in a list to match expected output format

    # Construct the response
    response = {
        "is_success": True,
        "user_id": user_details["user_id"],
        "email": user_details["email"],
        "roll_number": user_details["roll_number"],
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    
    return jsonify(response)

# GET method endpoint
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if _name_ == '_main_':
    app.run(debug=True)
