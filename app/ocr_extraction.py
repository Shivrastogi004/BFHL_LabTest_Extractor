import easyocr

# Initialize EasyOCR Reader only once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image_path):
    """
    Extract text from an image using EasyOCR.
    """
    results = reader.readtext(image_path, detail=0)
    # Join extracted lines into a single text string
    return "\n".join(results)
