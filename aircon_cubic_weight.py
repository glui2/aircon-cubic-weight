import requests

# Hit Kogan API
print(f'Sending GET request to API...')
kogan_url = f'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'


def get_aircon_objects(api_stem):
    api = kogan_url + api_stem
    response = requests.get(api)
    data = response.json()
    aircon_objects = []
    if data['next']:
        # recursive case: run this code until no more items to list
        new_stem = data['next']
        print(new_stem)
        aircon_objects = get_aircon_objects(new_stem)

    else:
        # base case: start returning aircon objects once there are no more items to list
        print("end of list!")

    current_aircon_objects = [product_object for product_object in data['objects']
                              if product_object['category'] == 'Air Conditioners']

    all_aircon_objects = current_aircon_objects + aircon_objects
    print(all_aircon_objects)
    return all_aircon_objects


get_aircon_objects(f'/api/products/1')
