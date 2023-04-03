import unittest

from perfometrics.status_checker import StatusChecker
from perfometrics.curl import CurlUptime


class TestCurl(unittest.TestCase):
    
    def test_status(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertEqual(curl.get_status(), 200)
    
    def test_dns_lookup(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertGreaterEqual(curl.get_dns_lookup(), 0)

    def test_tcp(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertGreaterEqual(curl.get_tcp(), 0)

    def test_ssl_tls(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertGreaterEqual(curl.get_ssl_tls(), 0)

    def test_ttfb(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertGreaterEqual(curl.get_ttfb(), 0)
    
    def test_data_transfer(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertGreaterEqual(curl.get_data_transfer(), 0)
    
    def test_total(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertGreaterEqual(curl.get_total(), 0)

    def test_metrics(self):
        url = 'https://alixo.ir'
        curl = CurlUptime(url)
        self.assertIs(type(curl.get_metrics()), dict)

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