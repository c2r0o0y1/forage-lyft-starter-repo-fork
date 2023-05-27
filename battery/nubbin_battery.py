from .battery import Battery
# from add_date import add_years_to_date
from datetime import timedelta

class NubbinBattery(Battery):
    def __init__(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def need_service(self) -> bool:
        date_which_battery_should_be_serviced_by = self.last_service_date + timedelta(days=365*4)
        return date_which_battery_should_be_serviced_by < self.current_date
