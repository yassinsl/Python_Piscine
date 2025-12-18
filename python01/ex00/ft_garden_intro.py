def ft_graden_intro():
    print("=== Welcome to My Garden ===");
    plant = input("Please Enter Name Of Plant: ");
    age = int(input("Please Enter the age: "));
    Height = int(input("Please Enter the height: "));
    print(f"Planet: {plant}", f"age: {age} days", f"Height: {Height} cm", sep="\n");
if __name__ == "__main__":
    ft_graden_intro();
