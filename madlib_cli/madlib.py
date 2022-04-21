
def read_template(file_path):
    try:
        with open(file_path, 'r') as doc:
            return doc.read()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    stripped = ""
    parts = []
    capture = False
    current_part = ""

    for char in template:
        if char == '{':
            stripped += char
            capture = True
            current_part = ""
        elif char == '}':
            stripped += char
            capture = False
            parts.append(current_part)
        elif capture:
            current_part += char
        else:
            stripped += char

    return stripped, tuple(parts)


def merge(template, tupl):
    return template.format(*tupl)


read_template('../assets/dark_and_stormy_night_template.txt')
