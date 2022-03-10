import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
from common import vars as v
from common.utils import s_response


class TestUtils(unittest.TestCase):
    good_request = {
        v.ACTION: v.PRESENCE,
        v.TIME: True,
        v.USER: {
            v.ACCOUNT_NAME: 'Guest'
        }
    }

    bad_request = {
        v.ACTION: 'message',
        v.TIME: True,
        v.USER: {
            v.ACCOUNT_NAME: 'Guest'
        }
    }

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_good_server_response(self):
        self.assertEqual(s_response(self.good_request), {v.RESPONSE: 200})

    def test_bad_server_response(self):
        self.assertEqual(s_response(self.bad_request), {v.RESP_DEFAULT_IP_ADDR: 400, v.ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
