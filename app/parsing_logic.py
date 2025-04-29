import re
from app.utils import check_out_of_range

def parse_lab_tests(extracted_text):
    results = []
    lines = extracted_text.split('\n')
    current_test_name = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Clean line
        line = re.sub(r'\[.*?\]', '', line)
        line = line.replace(':', ' ').replace('  ', ' ')

        # If line has only text and no numbers → assume it's a Test Name
        if re.match(r'^[A-Za-z\s\(\)\-\/]+$', line):
            current_test_name = line
            continue
        
        # If line contains value + unit + range
        match = re.search(r'([\d.]+)\s+([a-zA-Z/%μg\/dL]+)\s+([\d.]+\s*-\s*[\d.]+)', line)
        if match and current_test_name:
            try:
                test_value = float(match.group(1))
                test_unit = match.group(2).strip()
                bio_reference_range = match.group(3).replace(' ', '')

                is_out_of_range = check_out_of_range(test_value, bio_reference_range)

                results.append({
                    "test_name": current_test_name,
                    "test_value": test_value,
                    "bio_reference_range": bio_reference_range,
                    "test_unit": test_unit,
                    "lab_test_out_of_range": is_out_of_range
                })

                # Reset current test name
                current_test_name = ""

            except:
                continue

    return results
