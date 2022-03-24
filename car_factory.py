
from . import Car

from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery

class Car_factory:

    @staticmethod
    def car_calliope(date_today, last_service_date, current_milage, last_service_milage):
        engine  = CapuletEngine(current_milage,last_service_milage)
        battery = SpindlerBattery(date_today,last_service_date)
        check  = Car(battery,engine)
        return check


    @staticmethod
    def car_glissade(date_today, last_service_date, current_milage, last_service_milage):
        engine  = WilloughbyEngine(current_milage,last_service_milage)
        battery = SpindlerBattery(date_today,last_service_date)
        check  = Car(battery,engine)
        return check

    @staticmethod
    def car_palindrome(date_today, last_service_date,indicator_on_off):
        engine  = SternmanEngine(indicator_on_off)
        battery = SpindlerBattery(date_today,last_service_date)
        check  = Car(battery,engine)
        return check

    @staticmethod
    def car_rorschach(date_today, last_service_date, current_milage, last_service_milage):
        engine  = WilloughbyEngine(current_milage,last_service_milage)
        battery = NubbinBattery(date_today,last_service_date)
        check  = Car(battery,engine)
        return check

    
    @staticmethod
    def car_thovex(date_today, last_service_date, current_milage, last_service_milage):
        engine  = CapuletEngine(current_milage,last_service_milage)
        battery = NubbinBattery(date_today,last_service_date)
        check  = Car(battery,engine)
        return check


