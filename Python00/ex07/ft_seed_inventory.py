def ft_seed_inventory(data, number, information):
        if information == "Packets": 
            print(data.capitalize(), "seeds:", number, information, "available", sep=" ")
        elif information == "grams": 
            print(data.capitalize(), "seeds:", number, information, "total", sep=" ")
        elif information == "area":
            print(data.capitalize(), "seeds:","cover", number, "square metter", sep=" ")
        else:
            print(data.capitalise, "seeds:", number, "unknown unit type", sep=" ")

if __name__ == "__main__":
    ft_seed_inventory("tomato", 15, "Packets");
    ft_seed_inventory("carrot", 8, "grams");
    ft_seed_inventory("lettuce", 12, "area");
