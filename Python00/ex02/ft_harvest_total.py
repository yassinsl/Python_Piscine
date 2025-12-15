def ft_harvest_total():
    arr=[0] * 3;
    for i in range(3):
        arr[i] =int(input(f"Day {i} harvest: "));
    print("Total harvest: ", arr[0] +arr[1] + arr[2]);

if __name__ =="__main__":
    ft_harvest_total();
