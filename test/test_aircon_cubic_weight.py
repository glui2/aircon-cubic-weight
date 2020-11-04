import unittest
from aircon_cubic_weight import calculate_cubic_weight, get_aircon_objects


class TestAirconCubicWeight(unittest.TestCase):

    # tests the calculate_cubic_weight method, assuming conversion factor of 205, 1m  x 2m x 5m parcel should have a cubic weight of 2500kg
    def test_calculate_cubic_weight(self):
        # act
        test_product_object = {'category': 'Air Conditioners', 'title': 'Window Seal for Portable Air Conditioner Outlets',
                               'weight': 235.0, 'size': {'width': 100, 'length': 200, 'height': 500}}
        # arrange
        test_cubic_weight = calculate_cubic_weight(test_product_object)

        # assert
        self.assertEqual(test_cubic_weight, 2500)

    # tests the get_aircon_objects method, using the last api in which an object with category "Air Conditioners" occurs, should only return a list of 2 objects with "Air Conditioners" as category
    def test_get_aircon_objects(self):

        # act
        test_api = "/api/products/a"

        # arrange
        test_aircon_objects = get_aircon_objects(test_api)
        number_of_aircon_objects = sum(
            aircon_object['category'] == "Air Conditioners" for aircon_object in test_aircon_objects)

        # assert
        self.assertEqual(number_of_aircon_objects, 2)

    # integration test
    def test_aircon_cubic_weight(self):
        # act
        test_api = "/api/products/a"

        # arrange
        test_aircon_objects = get_aircon_objects(test_api)
        cubic_weights = [calculate_cubic_weight(
            aircon_object) for aircon_object in test_aircon_objects]
        average_cubic_weight = sum(cubic_weights)/len(cubic_weights)

        # assert (accuracy to 5dp for testing purposes)
        self.assertAlmostEqual(average_cubic_weight, 61.44960938, 5)


if __name__ == '__main__':
    unittest.main()
