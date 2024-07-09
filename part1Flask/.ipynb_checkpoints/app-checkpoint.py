from flask import Flask, request, jsonify, send_file
from PIL import Image
import io
import random

app = Flask(__name__)

@app.route('/')
def index():
    usage_instructions = """
    Welcome to the Flask Image Converter App!

    Available Routes:
    1. /convert (POST): Convert an image from one type to another.
       - Usage: Send a POST request with 'image' (file) and 'output_type' (str) as form data.
       - Supported output types: ['jpeg', 'png', 'bmp', 'gif', 'tiff']

    2. /random-number: Generate a random number within a given range.
       - Usage: Send a GET request with 'min' and 'max' as query parameters.
    """
    return usage_instructions

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files or 'output_type' not in request.form:
        return jsonify({"error": "Please provide the image file and output type"}), 400

    image_file = request.files['image']
    output_type = request.form['output_type']

    if output_type not in ['jpeg', 'png', 'bmp', 'gif', 'tiff']:
        return jsonify({"error": "Unsupported output type"}), 400

    try:
        image = Image.open(image_file.stream)
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=output_type.upper())
        img_byte_arr.seek(0)
        return send_file(img_byte_arr, mimetype=f'image/{output_type}')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/random-number')
def random_number():
    min_val = request.args.get('min', default=0, type=int)
    max_val = request.args.get('max', default=100, type=int)
    if min_val > max_val:
        return jsonify({"error": "min should be less than or equal to max"}), 400

    random_num = random.randint(min_val, max_val)
    return jsonify({"random_number": random_num})

if __name__ == '__main__':
    app.run(debug=True)
