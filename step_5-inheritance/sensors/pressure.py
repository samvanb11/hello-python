from .sensor import Sensor


class PressureSensor(Sensor):
    def __init__(self, name):
        Sensor.__init__(self, name)

    def get_value(self):
        # Go and get the pressure from the hardware
        return 1080
