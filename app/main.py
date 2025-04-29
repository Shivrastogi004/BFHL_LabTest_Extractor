from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ocr_extraction import extract_text_from_image
from parsing_logic import parse_lab_tests

import os, uuid, shutil, json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = extract_text_from_image(file_path)
        parsed_data = parse_lab_tests(text)

        json_filename = f"{file_id}.json"
        json_path = os.path.join(OUTPUT_DIR, json_filename)
        with open(json_path, "w") as json_file:
            json.dump({"is_success": True, "data": parsed_data}, json_file, indent=4)

        return FileResponse(json_path, media_type='application/json', filename="lab_report_output.json")
    except Exception as e:
        return JSONResponse(status_code=500, content={"is_success": False, "error": str(e)})
