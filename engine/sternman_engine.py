from abc import ABC

from car import Car
from.engine import Engine


class SternmanEngine(Car, ABC):
    def __init__(self, indicator_on_off):
        self.indicator_on_off = indicator_on_off

    def needs_service(self):
        if self.indicator_on_off:
            return True
        else:
            return False
