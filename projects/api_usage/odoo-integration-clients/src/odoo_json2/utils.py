__author__ = 'Joan A. Pinol  (japinol)'

def read_file_as_string(file_name):
    res = []
    try:
        with open(file_name, "r", encoding='utf-8') as in_file:
            for line_in in in_file:
                res.append(line_in)
    except FileNotFoundError:
        print(f"Warning: Input file not found: {file_name}")
    except Exception:
        print(f"Warning: Error reading file: {file_name}")

    return ''.join(res)
