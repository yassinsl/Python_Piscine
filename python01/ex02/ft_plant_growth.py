class Plants:
    def __init__(self, name, age, hieght):
        self.name = name;
        self.age_grow = age;
        self.hieght = hieght;
    def grow(self):
        self.hieght+=1;
    def age(self):
        self.age_grow+=1;
    def get_info(self):
        return f"Name: {self.name}, Height: {self.height}cm, Age: {self.age_grow} days"

if __name__ == "__main__":
    p = Plants("Rose", 30, 25);
    p.grow()
    p.age()
    print(f"{p.name} : {p.hieght}cm, {p.age_grow} days old");
