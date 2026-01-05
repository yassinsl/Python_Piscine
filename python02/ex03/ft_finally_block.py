class ErrorWatering(Exception):
    def __init__(self, msg):
        super().__init__(msg);
def water_open(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ErrorWatering(f"Error: Cannot water '{plant}' invalid plants!")
            else : print(f"watering {plant}");
    except ErrorWatering as e:
        print(e);
    finally:
        print("closing watering system(cleanup)")
def test_watering_system():
    print("Testing normal watering")
    plants = ["tomatos", "carrots", "lettuce"]
    water_open(plants);
    print("watering completed successfully")
    print("Testing with error...")
    plants = ["tomatos", None, "lettuce"]
    water_open(plants);
    print("Cleanup always happens. even with errors")
            
if __name__== "__main__":
    print("Graden Watering System")
    test_watering_system()
