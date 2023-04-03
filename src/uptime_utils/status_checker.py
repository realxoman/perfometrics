from uptime_utils.domain_checker import DomainChecker
from uptime_utils.decorators import *

class StatusChecker:

    def __init__(self, url) -> None:
        self.url = url
    
    @time_of_execution
    def check_status(self):
        self.checker = DomainChecker(self.url).send_request()
        self.status = self.checker.status_code
        return self.validation()
    
    def validation(self):
        if self.status == 200:
            return True
        return False