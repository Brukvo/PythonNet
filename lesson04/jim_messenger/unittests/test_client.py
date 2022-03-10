import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
from common import vars as v
from client import presence, parse_resp


class TestClient(unittest.TestCase):
    presence_success = {
        v.ACTION: v.PRESENCE,
        v.TIME: 1646660089.3014915,
        v.USER: {
            v.ACCOUNT_NAME: 'Guest'
        }
    }

    response_success = {v.RESPONSE: 200}
    response_fail = {v.RESPONSE: 400, v.ERROR: 'Fail'}

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_presence_success(self):
        self.assertEqual(presence(unittest=True), self.presence_success)

    def test_presence_fail(self):
        self.assertEqual(presence(unittest=True), self.presence_success)

    def test_response_ok(self):
        self.assertEqual(parse_resp(self.response_success), '200: OK')

    def test_response_fail(self):
        self.assertEqual(parse_resp(self.response_fail), '400: Fail')


if __name__ == '__main__':
    unittest.main()
