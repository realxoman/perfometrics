import unittest

from uptime_utils.status_checker import StatusChecker
from uptime_utils.curl import CurlUptime


class TestCurl(unittest.TestCase):
    url = 'https://alixo.ir'
    curl = CurlUptime(url)

    def test_status(self):
        self.assertEqual(self.curl.get_status(), 200)
    
    def test_dns_lookup(self):
        self.assertGreaterEqual(self.curl.get_dns_lookup(), 0)

    def test_tcp(self):
        self.assertGreaterEqual(self.curl.get_tcp(), 0)

    def test_ssl_tls(self):
        self.assertGreaterEqual(self.curl.get_ssl_tls(), 0)

    def test_ttfb(self):
        self.assertGreaterEqual(self.curl.get_ttfb(), 0)
    
    def test_data_transfer(self):
        self.assertGreaterEqual(self.curl.get_data_transfer(), 0)
    
    def test_total(self):
        self.assertGreaterEqual(self.curl.get_total(), 0)

    def test_metrics(self):
        self.assertIs(type(self.curl.get_metrics()), type(dict))

class TestStatusChecker(unittest.TestCase):
    
    def test_status_true(self):
        url = 'https://alixo.ir'
        state = StatusChecker(url)
        self.assertTrue(state.check_status())

    def test_status_false(self):
        url = 'http://forbit.ddd'
        state = StatusChecker(url)
        self.assertFalse(state.check_status())

if __name__ == '__main__':
    unittest.main()