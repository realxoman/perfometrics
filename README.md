# Perfometrics

Perfometrics is a Python library for measuring the performance of a given URL using the pycurl library. The library provides various metrics such as HTTP status code, time taken for DNS resolution, time taken for establishing TCP connection, time taken for establishing SSL/TLS connection, time taken for the first byte of the response, time taken for data transfer, and total time taken for the request.

## Installation

To install perfometrics, simply run the following command:

```bash
pip install perfometrics
```

## Usage

To use perfometrics, you can import the curl module and create a CurlUptime object with the URL you want to measure. Here's an example:

```python
import perfometrics.curl as pcurl

url = 'https://example.com'
curl_uptime = pcurl.CurlUptime(url)
metrics = curl_uptime.get_metrics()

print('Metrics for', url)
print('HTTP status code:', metrics['status_code'])
print('Time taken for DNS resolution:', metrics['dns_lookup'], 'seconds')
print('Time taken for establishing TCP connection:', metrics['tcp'], 'seconds')
print('Time taken for establishing SSL/TLS connection:', metrics['ssl_tls'], 'seconds')
print('Time taken for the first byte of the response:', metrics['ttfb'], 'seconds')
print('Time taken for data transfer:', metrics['data_transfer'], 'seconds')
print('Total time taken for the request:', metrics['total'], 'seconds')
```

This will output something like:

```
Metrics for https://example.com
HTTP status code: 200
Time taken for DNS resolution: 0.003439 seconds
Time taken for establishing TCP connection: 0.057725 seconds
Time taken for establishing SSL/TLS connection: 0.09169 seconds
Time taken for the first byte of the response: 0.213251 seconds
Time taken for data transfer: 0.067498 seconds
Total time taken for the request: 0.282891 seconds
```

After you're done with the CurlUptime object, you should call its close_session() method to close the pycurl.Curl() session.

## License

perfometrics is licensed under the GNU General Public License v3.0. See the LICENSE file for more information.