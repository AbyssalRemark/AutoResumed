import re

def convert_to_snake(data):
    snake_dict = {}
    for key, value in data.items():
        new_key = re.sub("([a-z0-9])([A-Z])", r"\1_\2", key).lower()
        if isinstance(value, dict):
            snake_dict[new_key] = convert_to_snake(value)
        elif isinstance(value, list):
            if all(isinstance(item, dict) for item in value):
                snake_dict[new_key] = [convert_to_snake(item) for item in value]
            elif all(isinstance(item, str) for item in value):
                snake_dict[new_key] = value
        else:
            snake_dict[new_key] = value
    return snake_dict

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
    _local_dict = {"name": "John Doe","label": [{"tags":["tag"],"label":"Programmer"}],"image": "https://somesite.tld/img.png","email": "john@gmail.com","phone": "(912) 555-4321","url": "https://johndoe.com","summary": [{"tags":["tag"],"summary":"A summary of John Doe…"}],"location": {"address": "2712 Broadway St","postal_code": "CA 94115","city": "San Francisco","countryCode": "US","region": "California"},"profiles": [{"tags": ["tag"],"network": "Twitter","username": "john","url": "https://twitter.com/john"}]}

    snake_case_dict = convert_to_snake(camel_case_dict)
    print(snake_case_dict)
    print(convert_to_snake(_local_dict))