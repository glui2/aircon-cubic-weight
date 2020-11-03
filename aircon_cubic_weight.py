import requests

############################ function definitions ############################

# Function: calculate_cubic_weight
# Inputs: takes an object from the Kogan API as an input
# Purpose: calculates the cubic weight based on the dimensions specified in the object
# Returns: cubic weight


def calculate_cubic_weight(product):
    # define length, height and width of the parcel (convert to metres).
    product_dimensions = product['size']
    length = product_dimensions['length']/100
    width = product_dimensions['width']/100
    height = product_dimensions['height']/100

    # use standard cubic weight conversion factor of 250.
    conv_factor = 250

    # calculate cubic weight
    cubic_weight = length*width*height*conv_factor
    return cubic_weight

# Function: get_aircon_objects
# Inputs: takes a string containing api stem ending
# Purpose: recursive function that appends the stem to the Kogan provided URL, and retrieves any object that has category of 'Air Conditioners'
# Returns: list of all objects in the 'Air Conditioners' category


def get_aircon_objects(api_stem):

    # form the api and retrieve data using a GET request
    kogan_url = f'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
    api = kogan_url + api_stem
    print(f'GET aircon objects from {api}')
    response = requests.get(api)
    data = response.json()
    aircon_objects = []

    if data['next']:
        # recursive case: run through object lists until no more items to list
        new_stem = data['next']
        aircon_objects = get_aircon_objects(new_stem)

    # retrieve any objects from 'Air Conditioners' category
    current_aircon_objects = [product_object for product_object in data['objects']
                              if product_object['category'] == 'Air Conditioners']

    # return cumulative list of aircon objects
    all_aircon_objects = current_aircon_objects + aircon_objects
    return all_aircon_objects


############################ Main ############################

# form list of aircon objects
aircon_object_list = get_aircon_objects(f'/api/products/1')

# calculate cubic weights of aircon objects
cubic_weights = [calculate_cubic_weight(
    aircon_object) for aircon_object in aircon_object_list]

# calculate average cubic weight of all aircon objects
average_cubic_weight = sum(cubic_weights)/len(cubic_weights)
print(
    f"Average cubic weight of products in the Air-Conditioner category is: {average_cubic_weight} kg")
