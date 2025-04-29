def check_out_of_range(test_value, ref_range):
    try:
        min_val, max_val = map(float, ref_range.split('-'))
        return not (min_val <= test_value <= max_val)
    except Exception:
        return True  # If parsing fails, assume out of range
