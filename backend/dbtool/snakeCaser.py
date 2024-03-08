import re

def convert_to_snake(data):
    required_dict = {}
    for key, value in data.items():
        if isinstance(value, str):
            new_key = re.sub("([a-z0-9])([A-Z])", r"\1_\2", key).lower()
            required_dict[new_key] = value
        elif isinstance(value, list) and all(isinstance(item, str) for item in value):
            new_key = re.sub("([a-z0-9])([A-Z])", r"\1_\2", key).lower()
            required_dict[new_key] = value
        elif isinstance(value, list) and all(isinstance(item, dict) for item in value):
            new_key = re.sub("([a-z0-9])([A-Z])", r"\1_\2", key).lower()
            required_dict[new_key] = [convert(item) for item in value]
    return required_dict

if __name__ == "__main__":
    # Example usage:
    camel_case_dict = {
        'firstName': 'Alice',
        'lastName': 'Smith',
        'addressDetails': {
            'streetAddress': '123 Main St',
            'cityName': 'New York'
        },
        'phoneNumbers': ['123-456-7890', '987-654-3210']
    }

    snake_case_dict = convert(camel_case_dict)
    print(snake_case_dict)