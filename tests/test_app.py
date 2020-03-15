import requests
import unittest

from werkzeug.datastructures import FileStorage


class ModelManagerTests(unittest.TestCase):

    url = "http://localhost:5053"

    def test_1(self):
        """ Test image upload """
        data = {
            'name': 'test_123',
        }

        files = {'file':  open('./tests/test_img.jpg', 'rb')}

        response = requests.post(f"{self.url}/", data=data, files=files)
        self.assertEqual(response.status_code, 200)

    def test_2(self):
        """ Test img exists """
        response = requests.get(f"{self.url}/img/test_123")
        self.assertEqual(response.status_code, 200)

    def test_3(self):
        """ Test img exists """
        response = requests.get(f"{self.url}/image/test_123")
        self.assertEqual(response.status_code, 200)

    def test_4(self):
        """ Test img don't exists """
        response = requests.get(f"{self.url}/image/test_000")
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
