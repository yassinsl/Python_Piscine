class GardenManager:
        def __init__();
class Garden:
    def __init__(self, plants, total_growth, type_of_plants)
        self._plants = plants;
        self._total_growth = total_growth;
        self._type_of_plants = type_of_plants
class Plant:
    def __init__(self,name, hieght, age):
        self._name = name;
        self._hieght = hieght;
        self._age = age;
class FloweringPlant(Plant):
    def __init__(self, name, hieght, age, folower_color,bloom_status):
        super().__init(name, hieght, age);
        self._folower_color = folower_color;
        self._bloom_status = bloom_status;
class PrizeFlower(FloweringPlant):
    def __init__(self, name, hieght, age, prize_point, score):
        super().__init__(self, name, age);
        self._prize_point = prize_point;
        self._score = score;
