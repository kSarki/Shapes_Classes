from parkingticket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, parked_car, parking_meter):
        illegal_minutes = parked_car.minutes_parked - parking_meter.minutes_purchased
        if illegal_minutes > 0:
            return ParkingTicket(parked_car, self, illegal_minutes)
        else:
            return None
