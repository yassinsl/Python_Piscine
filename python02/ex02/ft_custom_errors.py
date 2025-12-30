class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health
        super().__init__(f"PlantError: {name} is wilting")

    def test_plant(self):
        if self.age < 0 or self.health == "bad":
            raise PlantError(self.name, self.age, self.health)


class WaterError(GardenError):
    def __init__(self, amount):
        self.amount = amount
        super().__init__("WaterError: Not enough water")

    def test_water(self):
        if self.amount < 0:
            raise WaterError(self.amount)


if __name__ == "__main__":
    plant = PlantError("Tomatoes", -11, "good")

    try:
        plant.test_plant()
        print("Test Plants: successful")
    except PlantError as e:
        print(e.name)

