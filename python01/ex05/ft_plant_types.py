import math 

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
        print(f"{self._name} (Flower): {super().get_age()}cm, {super().get_hieght()} days, {self._color} ");
class Tree(Plants):
    def __init__(self,name, hieght , age, Trunck_diameter):
        super().__init__(name, hieght, age);
        self._Trunck_diameter= Trunck_diameter;
    def produce_shade(self):
        if self._Trunck_diameter <= 0:
            print("No shade [invalid tree size]");
        else :
            shad_area = 3.14 * math.pow(10 * self._Trunck_diameter, 2);
            print(f"{self._name} provides {shad_area} square metter of chade");
    def get_info(self):
        print(f"{self._name} (Tree): {super().get_age()}, {super().get_hieght()}, {self._Trunck_diameter}cm diameter");
class Vegetable(Plants):
    def __init__(self, name,hieght, age, harvest_var, nutritional_value):
        super().__init__(name, hieght, age);
        self._harvest_var = harvest_var;
        self._nutritional_value = nutritional_value;
    def  get_nutritional_value(self):
        print(f"{self._name} is rich in {self._nutritional_value}");
    def get_info(self):
        print(f"{self._name} (vegetable): {super().get_age()}, {super().get_hieght()}, {self._harvest_var} sumerr harvest");

if __name__ == "__main__":
    flower = Flower("Rose", 25, 30, "red");
    flower.get_info();
    flower.bloom();
    tree = Tree("Oak", 500, 1835, 50);
    tree.produce_shade();
    vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C");
    vegetable.get_info();
    vegetable.get_nutritional_value();
    
