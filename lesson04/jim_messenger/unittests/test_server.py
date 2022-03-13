import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
import common.vars as v
from common.utils import s_response


class TestServer(unittest.TestCase):
    bad_response_404 = {
        v.RESPONSE: 400,
        v.ERROR: 'Bad Request'
    }

    good_response = {v.RESPONSE: 200}

    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_good_response(self):
        self.assertEqual(s_response({
            v.ACTION: v.PRESENCE,
            v.TIME: 1.2,
            v.USER: {v.ACCOUNT_NAME: 'Guest'}
        }), self.good_response)

    def test_no_action_response(self):
        self.assertEqual(s_response({
            v.TIME: 1.2,
            v.USER: {v.ACCOUNT_NAME: 'Guest'}
        }), self.bad_response_404)


if __name__ == '__main__':
    unittest.main()
