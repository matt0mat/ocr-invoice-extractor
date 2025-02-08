# OCR Invoice Extractor

A simple Flask API for extracting text from invoice images using Tesseract OCR. This project demonstrates automated invoice processing by allowing users to upload images and receive structured text output.

## Features
✅ Upload invoice images (JPG, PNG, PDF*)  
✅ Extract text using Tesseract OCR  
✅ Return structured JSON response  

## Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ocr-invoice-extractor.git
cd ocr-invoice-extractor
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the Flask Server
```bash
python app.py
```

### 4️⃣ Test the API
Use `curl` or Postman to send a request:
```bash
curl -X POST -F "file=@invoice.png" http://127.0.0.1:5000/upload
```

## Example JSON Response
```json
{
  "extracted_text": "Invoice #12345, Total: $250.00, Date: 2024-02-08"
}
```

## Contributing
Feel free to fork this repo and enhance the functionality!

## License
MIT License

