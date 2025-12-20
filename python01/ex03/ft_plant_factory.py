class Plants:
    def __init__(self, name, hieght, age):
        self.name = name;
        self.hieght = hieght;
        self.age = age;
    def get_info(self): 
        print(f"Created: {self.name} ({self.hieght }cm, {self.age} days)")
def ft_plant_factory():
    plants_arr = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)
            ];
    plants = [];
    for name, hieght, age in plants_arr:
        plants.append(Plants(name, hieght, age));
    return plants;
if __name__== "__main__":
    plants  = ft_plant_factory();
    for plant in plants:
        plant.get_info();
