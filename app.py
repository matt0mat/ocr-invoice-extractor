import pytesseract
from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend to access the API
from PIL import Image
import io
import logging

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests

# Inside Docker, Tesseract is in /usr/bin/tesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Set up logging for better debugging
logging.basicConfig(level=logging.INFO)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logging.error("No file uploaded")
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read()))
        extracted_text = pytesseract.image_to_string(image)
        logging.info("OCR Extraction Successful")
        return jsonify({"extracted_text": extracted_text})
    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
