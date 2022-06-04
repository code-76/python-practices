
import unittest

from unittest.mock import patch
from utils.hkjc import HKJCRequest
import json

class TestRemoteNumberDataSource(unittest.TestCase):

    def test_hkjc_request(self):
        mock_file = open('testcase\mock\search_result.json')
        mock_json = json.load(mock_file)

        with patch('utils.hkjc.HKJCRequest.get') as mock_get:
            mock_get.status_code = 200
            mock_get.content = mock_json

            hkjc_request = HKJCRequest()
            response = hkjc_request.get

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, mock_json)