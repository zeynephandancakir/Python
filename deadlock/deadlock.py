class Car:
    def __init__(self):
        self.fuel = 0

    def drive(self):
        if self.fuel > 0:
            print("Car is driving to the gas station.")
            self.fuel -= 1
            print("Car has reached the gas station.")
        else:
            print("Car cannot drive. Out of fuel.")

    def refuel(self):
        if self.fuel == 0:
            print("Deadlock detected: Car needs fuel to reach the gas station.")
        else:
            print("Car is refueling at the gas station.")
            self.fuel += 1

def main():
    car = Car()
    car.drive()
    car.refuel()
    # Deadlock durumunu göstermek için bir kez daha kontrol edelim
    car.drive()
    car.refuel()

if __name__ == "__main__":
    main()

