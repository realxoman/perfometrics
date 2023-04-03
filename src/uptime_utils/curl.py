import pycurl

class CurlUptime:
    '''
    This code defines a CurlUptime class that measures various metrics for a given URL using the pycurl library. The class constructor takes a URL as an argument and initializes a pycurl.Curl() session with the specified URL. Various options are set for the session such as NOBODY to avoid downloading the body of the response. The perform() method is then called to execute the session.

    The class defines several methods to retrieve different metrics such as get_status() to get the HTTP status code, get_dns_lookup() to get the time taken for DNS resolution, get_tcp() to get the time taken for establishing the TCP connection, get_ssl_tls() to get the time taken for establishing the SSL/TLS connection, get_ttfb() to get the time taken for the first byte of the response, get_data_transfer() to get the time taken for the data transfer, and get_total() to get the total time taken for the request.

    The get_metrics() method returns a dictionary of all the metrics, and the close_session() method is called to close the pycurl.Curl() session.

    Overall, this code is useful for measuring the performance of a given URL, particularly for debugging purposes.
    '''
    def __init__(self, url) -> None:
        # Initialize class with given URL and create a pycurl session.
        self.url = url
        self.curl_session = pycurl.Curl()
        # Set URL for pycurl session.
        self.curl_session.setopt(self.curl_session.URL, self.url)
        # Don't download the body of the response.
        self.curl_session.setopt(self.curl_session.NOBODY, 1)
        # Execute the pycurl session.
        self.curl_session.perform()
        # Get info function to retrieve metrics.
        self.getinfo = self.curl_session.getinfo

    def get_status(self):
        # Get HTTP status code.
        return (self.getinfo(self.curl_session.RESPONSE_CODE))
    
    def get_dns_lookup(self):
        # Get time taken for DNS resolution.
        return self.getinfo(self.curl_session.NAMELOOKUP_TIME)

    def get_tcp(self):
        # Get time taken for establishing TCP connection.
        return self.getinfo(self.curl_session.CONNECT_TIME) - self.getinfo(self.curl_session.NAMELOOKUP_TIME)

    def get_ssl_tls(self):
        # Get time taken for establishing SSL/TLS connection.
        return self.getinfo(self.curl_session.APPCONNECT_TIME) - self.getinfo(self.curl_session.CONNECT_TIME)

    def get_ttfb(self):
        # Get time taken for first byte of the response.
        return self.getinfo(self.curl_session.STARTTRANSFER_TIME) - self.getinfo(self.curl_session.PRETRANSFER_TIME)
    
    def get_data_transfer(self):
        # Get time taken for data transfer.
        return self.getinfo(self.curl_session.TOTAL_TIME) - self.getinfo(self.curl_session.STARTTRANSFER_TIME)
    
    def get_total(self):
        # Get total time taken for the request.
        return self.getinfo(self.curl_session.TOTAL_TIME)

    def get_metrics(self) -> dict:
        # Get all metrics as a dictionary.
        metrics = dict()
        metrics.update({
            'status_code': self.get_status(),
            'dns_lookup': self.get_dns_lookup(),
            'tcp': self.get_tcp(),
            'ssl_tls': self.get_ssl_tls(),
            'ttfb': self.get_ttfb(),
            'data_transfer': self.get_data_transfer(),
            'total': self.get_total()
        })
        self.close_session()
        return metrics
        

    def close_session(self):
        # Close the pycurl session.
        self.curl_session.close()

