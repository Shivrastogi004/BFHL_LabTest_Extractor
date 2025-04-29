import os
import json
from app.ocr_extraction import extract_text_from_image
from app.parsing_logic import parse_lab_tests

# Paths
input_folder = "lbmaske"
output_folder = "outputs"

# Create outputs folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image
for img_name in os.listdir(input_folder):
    if img_name.endswith(".png") or img_name.endswith(".jpg") or img_name.endswith(".jpeg"):
        img_path = os.path.join(input_folder, img_name)

        # OCR extraction
        try:
            text = extract_text_from_image(img_path)
            parsed_data = parse_lab_tests(text)

            # Final JSON structure
            final_json = {
                "is_success": True,
                "data": parsed_data
            }

            # Save JSON with same name
            json_filename = os.path.splitext(img_name)[0] + ".json"
            json_path = os.path.join(output_folder, json_filename)

            with open(json_path, "w") as f:
                json.dump(final_json, f, indent=4)

            print(f"Processed: {img_name} -> {json_filename}")

        except Exception as e:
            print(f"Failed processing {img_name}: {str(e)}")
