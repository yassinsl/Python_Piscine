class SecurePlants:
    def __init__(self, name, age, height):
        self.name = name;
        self._age_valid = True;
        self._height_valid = True;
        self.set_age(age);
        self.set_height(height); 
    def set_height(self, height):
        if height < 0: 
            print("f{height}cm  is Invalid Value [Rejected]")
            self.height_valid = False;
        else : self._height = height;
    def set_age(self, age):
        if age < 0:
            print(f"{age} days  is Invalid Value [Rejected]")
            self._age_valid = False;
        else: self._age = age;
    def get_age(self): return self._age;
    def get_height(self) : return self._height;
    def get_info(self):
        print(f"plant created: {self.name}")
        if self._age_valid == True and self._height_valid == True:
            print( f"Height update: {self.get_height()} cm")
            print( f"Height update: {self.get_age()} cm")
        else :
            print(f" cannot find any value [Rejected]")
if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlants("Rose", 3, 30);
    plant.get_info();
    plant.set_age(-5);
    plant.set_age(100);
    print(f"new_age {plant.get_age()}");

