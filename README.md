# Lab Report OCR Extractor (FastAPI)

This project extracts lab test names, values, units, and biological reference ranges from medical lab report images using OCR (Tesseract) and returns the results in structured JSON format.

### 🔧 Features
- Upload lab report image via API or Web UI
- Extracts:
  - Test Name
  - Test Value
  - Reference Range
  - Unit
  - Out-of-range flag
- JSON file is automatically downloaded
- Built with **FastAPI**, **pytesseract**, and **JavaScript**

---

### 🚀 API Endpoint

**POST** `/get-lab-tests`

- Accepts: `multipart/form-data` with image file
- Returns: Downloadable `.json` containing extracted lab test data

---

### 💻 Local Setup

```bash
git clone https://github.com/Shivrastogi004/outputs.git
cd outputs

# Create and activate virtual environment (optional)
python -m venv venv
venv\\Scripts\\activate   # On Windows

# Install requirements
pip install -r requirements.txt

# Run FastAPI app
uvicorn main:app --reload
```
---
### 🌐 Frontend Web App
Open static/index.html in your browser

Upload lab report image

JSON will be automatically downloaded
---
