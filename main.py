from parked_car import ParkedCar
from parkingmeter import ParkingMeter
from police_officer import PoliceOfficer

def run_scenario(car, meter, officer, description):
    print(f"=== {description} ===")
    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket, "\n")
    else:
        print(f"{car} is legally parked.\n")

def main():
    # Scenario 1
    run_scenario(
        ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30),
        ParkingMeter(40),
        PoliceOfficer("John Doe", "5678"),
        "Scenario 1: Car Parked Legally"
    )

    # Scenario 2
    run_scenario(
        ParkedCar("Honda", "Accord", "Blue", "ABC987", 70),
        ParkingMeter(60),
        PoliceOfficer("Jane Smith", "1234"),
        "Scenario 2: Car Parked Illegally (Less Than an Hour Over)"
    )

    # Scenario 3
    run_scenario(
        ParkedCar("Ford", "Mustang", "Black", "LMN456", 190),
        ParkingMeter(60),
        PoliceOfficer("James Brown", "4321"),
        "Scenario 3: Car Parked Illegally (Multiple Hours Over)"
    )

    # Scenario 4: Multiple cars
    cars = [
        ParkedCar("Nissan", "Altima", "White", "JKL321", 60),
        ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80),
        ParkedCar("BMW", "X5", "Black", "BMW999", 500),
        ParkedCar("Toyota", "Corolla", "Gray", "AAA111", 45),
        ParkedCar("Honda", "Civic", "Blue", "BBB222", 70)
    ]
    meters = [
        ParkingMeter(60),
        ParkingMeter(60),
        ParkingMeter(60),
        ParkingMeter(50),
        ParkingMeter(65)
    ]
    officer4 = PoliceOfficer("Sarah Green", "9999")

    for i, (car, meter) in enumerate(zip(cars, meters), start=1):
        run_scenario(car, meter, officer4, f"Scenario 4.{i}: Car in Parking Lot")

if __name__ == "__main__":
    main()
