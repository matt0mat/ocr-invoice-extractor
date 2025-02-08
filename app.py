import pytesseract
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

# Inside Docker, Tesseract is in /usr/bin/tesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    try:
        image = Image.open(io.BytesIO(file.read()))
        extracted_text = pytesseract.image_to_string(image)
        return jsonify({"extracted_text": extracted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
