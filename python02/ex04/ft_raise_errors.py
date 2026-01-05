def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Error : Plant name cannot be empty")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high(max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low(min 1)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight {sunlight_hours} is too high (max 12)")
    return f"Plant {plant_name} is healty"
def test_plan_checks():
    try:
     print("Testing good value...")
     print(check_plant_health('tomato',10, 2 ))
    except ValueError as e:
        print(e)
    try:
     print("Testing empty plant name...")
     print(check_plant_health("", 5, 12))
    except ValueError as e:
        print(e)
    try:
     print("Testing bad water level...")
     print(check_plant_health("tomato", 15, 12))
    except ValueError as e:
        print(e)
    try:
     print("Testing bad sunlight...")
     print(check_plant_health("tomato", 1, 0))
    except ValueError as e:
        print(e)
    print("All error raiming tests complated")
    
            
if __name__== "__main__":
    print("=== Graden Plant Health Checker ===");
    test_plan_checks();
