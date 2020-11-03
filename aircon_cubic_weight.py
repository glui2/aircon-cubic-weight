import requests


def calculate_cubic_weight(product):
    # Cubic weight is calculated by multiplying the length, height and width of the parcel (metres).
    product_dimensions = product['size']
    length = product_dimensions['length']/100
    width = product_dimensions['width']/100
    height = product_dimensions['height']/100

    # The result is then multiplied by the industry standard cubic weight conversion factor of 250.
    conv_factor = 250

    cubic_weight = length*width*height*conv_factor
    return cubic_weight


def get_aircon_objects(api_stem):
    kogan_url = f'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
    api = kogan_url + api_stem
    print(f'GET aircon objects from {api}')
    response = requests.get(api)
    data = response.json()
    aircon_objects = []

    if data['next']:
        # recursive case: run this code until no more items to list
        new_stem = data['next']
        aircon_objects = get_aircon_objects(new_stem)

    current_aircon_objects = [product_object for product_object in data['objects']
                              if product_object['category'] == 'Air Conditioners']

    all_aircon_objects = current_aircon_objects + aircon_objects
    return all_aircon_objects


### Main ###

aircon_object_list = get_aircon_objects(f'/api/products/1')
print(
    f"List of all objects in the Air-Conditioner category: {aircon_object_list} \n")

cubic_weights = [calculate_cubic_weight(
    aircon_object) for aircon_object in aircon_object_list]
print(
    f"Cubic weight of each object in the Air-Conditioner category:\n {cubic_weights} \n")


average_cubic_weight = sum(cubic_weights)/len(cubic_weights)
print(
    f"Average cubic weight of products in the Air-Conditioner category is: {average_cubic_weight}")
