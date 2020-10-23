import unittest
from unittest.mock import patch

class Test_API(unittest.TestCase):
    @patch("iqvia_app.views.get_result")
    def test_get_result(self, mock):
        obj = mock()
        json_obj = {'result': 'modifications'}
        obj.get.return_value.data = json_obj
        response = obj.get('/Alzheimer Disease/14')
        self.assertEqual(response.data, json_obj)

if __name__ == "__main__":
    unittest.main()
