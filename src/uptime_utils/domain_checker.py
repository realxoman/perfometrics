import requests

class DomainChecker:
    '''
        Domain Checker:
        Send GET Request to domain.
        GET [Status , Content , Headers]
    '''
    def __init__(self, domain) -> None:
        self.domain = domain
        
    def send_request(self) -> object:
        self.request = requests.head(self.domain)
        return self.request
    
    