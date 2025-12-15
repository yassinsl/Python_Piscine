def ft_water_reminder():
    while(1):
        reminder = int(input("Days since last watering: "));
        if reminder < 0: print("Please Enter positive number :(: ");
        else:break;
    if reminder > 2: print("Water the plants");
    else: print("Plants are fine");
if __name__== "__main__":
    ft_water_reminder();
