import math

class ParkingTicket:
    def __init__(self, car, officer, illegal_minutes):
        self.car = car
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        # $25 for first hour or part, $10 for each additional hour or part
        hours_over = math.ceil(self.illegal_minutes / 60)
        if hours_over <= 1:
            return 25
        else:
            return 25 + (hours_over - 1) * 10

    def __str__(self):
        return (f"--- Parking Ticket ---\n"
                f"Car: {self.car}\n"
                f"Illegal Minutes: {self.illegal_minutes}\n"
                f"Fine: ${self.fine}\n"
                f"Issued by Officer {self.officer_name}, Badge {self.badge_number}")
