
import unittest

from unittest.mock import patch
from utils.hkjc import HKJCRequest
import json

class TestRemoteNumberDataSource(unittest.TestCase):

    def setUp(self):
        try:
            self.mock_file = open('testcase\mock\search_result.json')
            self.mock_json = json.load(self.mock_file)
        finally:
            self.mock_file.close()

    def tearDown(self):
        self.mock_file = None
        self.mock_json = None

    def test_hkjc_request(self):

        with patch('utils.hkjc.HKJCRequest.get') as mock_get:
            mock_get.status_code = 200
            mock_get.content = self.mock_json

            hkjc_request = HKJCRequest()
            response = hkjc_request.get

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, self.mock_json)