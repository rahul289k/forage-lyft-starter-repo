from servicable import Servicable

class Car(Servicable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine  = engine

# noe to check if either engine or battery needs service we define a function

    def needs_service(self):

        engine_needs_service = self.engine.needs_service()

        battery_needs_service = self.battery.needs_service()

        return engine_needs_service or battery_needs_service