class GardenManager:
    def __init__(self, gardens):
        self._gardens_der = {}
        key = 0
        for garden in gardens:
            self._gardens_der[key] = garden
            key += 1
            @staticmethod
                def calculate_statistics(gardens):
                    i = 0;
                    sum_total_growth = 0
                    for graden in gardens:
                        for plant in gardens._plants:
                            i+=1
                        sum_total_growth += gradens._total_growth;
                    return i, sum_total_growth;


class Garden:
    def __init__(self, plants, total_growth, type_of_plants):
        self._plants = []
        for plant in plants:
            self._plants.append(plant)
        self._total_growth = total_growth
        self._type_of_plants = type_of_plants
class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
class FloweringPlant(Plant):
    def __init__(self, name, height, age, flower_color, bloom_status):
        super().__init__(name, height, age)
        self._flower_color = flower_color
        self._bloom_status = bloom_status
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, flower_color, bloom_status, prize_point, score):
        super().__init__(name, height, age, flower_color, bloom_status)
        self._prize_point = prize_point
        self._score = score

