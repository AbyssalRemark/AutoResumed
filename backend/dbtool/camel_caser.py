def convert_to_camel(input_dict):
    def snake_to_camel_case(key):
        components = key.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    def convert_keys(data):
        if isinstance(data, dict):
            camel_dict = {}
            for key, value in data.items():
                new_key = snake_to_camel_case(key)
                new_value = convert_keys(value)
                camel_dict[new_key] = new_value
            return camel_dict
        elif isinstance(data, list):
            return [convert_keys(item) for item in data]
        else:
            return data

    return convert_keys(input_dict)

if __name__== "__main__":
    #  Example usage:
    snake_case_dict = {
        'first_name': 'Alice',
        'last_name': 'Smith',
        'age': 30,
        'address_details': {
            'street_address': '123 Main St',
            'city_name': 'New York'
        },
        'phone_numbers': ['123-456-7890', '987-654-3210']
    }

    camel_case_dict = convert(snake_case_dict)
    print(camel_case_dict)
