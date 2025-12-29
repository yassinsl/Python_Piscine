def ft_first_execption(tmp_str):
    try:
         check = int(tmp_str);
    except ValueError:
        print(f"Error: {tmp_str} is not a valid number");
        return -1;
    if check > 40:
        raise ValueError(f"Error: {check}°C is Too hot for plants (max 40)°C ");
    elif check < 0 :
        raise ValueError(f"Error: {check}°C is Too cold for plants (min 0)°C ");
    return check;
if __name__ == "__main__":
    while(1):
        tmp_str = input("Pls enter a temperature: ");
        try:
           num =  ft_first_execption(tmp_str);
           if num != -1:
                print(f"Success Temperature: {num}°C")
                break;
        except ValueError as e:
            print(e);
