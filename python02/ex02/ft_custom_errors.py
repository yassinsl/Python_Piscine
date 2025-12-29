class GardenError(Exception):
    def __init__(self, age, health, amount):
        self.age = age;
        self.health = health;
        self.amount = _amount
    def check_status(self):
        test_Plant(self.health, self.age)
        test_water(self.amount);
class PlantError(GardenError):
    def __init__(self , name, age, health):
        self._name = name;
        self._age;
        self._health = health
    def test_Plant(health, age):
        if(age < 0 or health == "bad")
            raise PlantError("Caught PlantError : The tomato Plant is wilting");j 
class WaterError(GardenError):
    def __init__(self, amount)
        self._amount = _amount;
def test_water(amount):
    if(amount < 0)
        raise PlantError("Caught PlantError : The tomato Plant is wilting");
