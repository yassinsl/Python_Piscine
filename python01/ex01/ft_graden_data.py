class Plants:
    def __init__(self, name, Height, age):
        self.name = name;
        self.Height = Height;
        self.age = age;
if __name__ == "__main__":
    p1 = Plants("Rose", 25, 30);
    print(p1.name,": ", f"{p1.Height} cm, {p1.age} days old");
    p2 = Plants("Sunflower", 80, 45);
    print(p2.name,": ", f"{p2.Height} cm, {p2.age} days old");
