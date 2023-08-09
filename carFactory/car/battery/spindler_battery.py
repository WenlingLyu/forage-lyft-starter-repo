from abc import ABC

from car import Car


class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date):
        self.current_date = datetime.now().date()
        self.last_service_mileage = last_service_mileage

    def battery_should_be_serviced(self):
        return self.current_date - timedelta(days=1460) >= self.last_service_date 