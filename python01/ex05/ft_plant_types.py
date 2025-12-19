class Plants:
    def __init__(self, name, hieght, age):
        self._name =  name;
        self._hieght = hieght;
        self._age = age;
    def get_age(self): return self._age;
    def get_hieght(self): return self._hieght;

class Flower(Plants):
    def __init__(self,name, hieght , age, color):
        super().__init__(name, hieght, age);
        self._color = color;
    def bloom(self):
        print(f"{self._name} is Blooming beautifully")
    def get_info(self):
        print(f"{self._name} (Flower): {super().get_age()}, {super().get_hieght()}, {self._color}");
class Tree(Plants):
    def __init__(self,name, hieght , age, Trunck_diameter):
        super().__init__(name, hieght, age);
        self._Trunck_diameter= Trunck_diameter;
    def produce_shade(self):
        if self._Trunck_diameter <= 0:
            print("No shade [invalid tree size]");
        else :
            shad_area = 3.14 * (10 * self._Trunck_diameter);
            print(f"{self._name} provides {shad_area} square metter of chade");
class Vegetable(Plants):
