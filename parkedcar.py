class ParkedCar:

    def __init__(self, make, model, color, license_number, minutes_parked=60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = minutes_parked  # private attribute

    @property
    def minutes_parked(self):
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value):
        if value <= 0:
            raise ValueError("Minutes parked must be positive.")
        self._minutes_parked = value

    def __str__(self):
        return f"{self.color} {self.make} {self.model} ({self.license_number}) parked for {self.minutes_parked} minutes"
