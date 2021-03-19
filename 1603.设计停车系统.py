class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lot = [0] * 4
        self.lot[1] = big
        self.lot[2] = medium
        self.lot[3] = small

    def addCar(self, carType: int) -> bool:
        if self.lot[carType] == 0:
            return False
        self.lot[carType] -= 1
        return True

