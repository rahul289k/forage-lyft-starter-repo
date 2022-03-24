from .battery import Battery
from check_year import check_year

class NubbinBattery(Battery):
    
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):

        last_date = check_year(self.last_service_date, 4)
        if last_date< self.current_date:
            return True
        else:
            return False
