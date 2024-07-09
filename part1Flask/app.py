# This is where the file is saved as an app.py file and then run with `python app.py` in the terminal or in the cell below.

# Import the Flask module and create an instance of the Flask class.
from flask import Flask, request, jsonify, send_file
from PIL import Image
import io
import random

app = Flask(__name__)

# Define a route for the index page.
@app.route('/')
def index():
    usage_instructions = """
    <h1>Welcome to my Assignment 3 Flask App!</h1>

    <h2>Available Routes:</h2>
    <ul>
        <li><b>/ (GET):</b> Index page (You are here!)
            <ul>
                <li><b>Usage:</b> Visit the index page to see the usage instructions.</li>
            </ul>
        </li>
        <li><b>/convert (POST):</b> Convert an image from one type to another.
            <ul>
                <li><b>Usage:</b> Send a POST request with 'image' (file) and 'output_type' (str) as form data.</li>
                <li><b>Supported output types:</b> ['jpeg', 'png', 'gif']</li>
            </ul>
        </li>
        <li><b>/random-number (GET):</b> Generate a random number within a given range.
            <ul>
                <li><b>Usage:</b> Send a GET request with 'min' and 'max' as query parameters.</li>
            </ul>
        </li>
    </ul>
    """
    return usage_instructions

# Define a route for the convert image endpoint.
@app.route('/convert', methods=['POST'])
def convert_image():
    # Check if the request is a POST request and if the image and output type are provided.
    if 'image' not in request.files or 'output_type' not in request.form:
        return jsonify({"error": "Please provide the image file and output type"}), 400

    # Get the image file and output type from the request.
    image_file = request.files['image']
    output_type = request.form['output_type']

    # Check if the output type is supported.
    if output_type not in ['jpeg', 'png', 'gif']:
        return jsonify({"error": "This is an uunsupported output type"}), 400
    # Try to convert the image to the specified output type and return the converted image as a file.
    try:
        image = Image.open(image_file.stream) # Open the image file.
        img_byte_arr = io.BytesIO() # Create a BytesIO object.
        image.save(img_byte_arr, format=output_type.upper()) # Save the image to the BytesIO object.
        img_byte_arr.seek(0) # Set the pointer to the beginning of the file.
        return send_file(img_byte_arr, mimetype=f'image/{output_type}') # Return the converted image as a file.
    except Exception as e: # If an error occurs, return the error message.
        return jsonify({"error": str(e)}), 500

# Define a route for the random number endpoint.
@app.route('/random-number')
def random_number():
    min_val = request.args.get('min', default=0, type=int)
    max_val = request.args.get('max', default=100, type=int)
    if min_val > max_val:
        return jsonify({"error": "The min number should be less than or equal to max!"}), 400

    # Generate a random number within the specified range and return it.
    random_num = random.randint(min_val, max_val)
    return jsonify({"random_number": random_num})

if __name__ == '__main__':
    app.run(debug=True)
