class Garden(Exception):
    def __init__(self, msg):
        super().__init__(msg);
class PlantError(Garden):
    def __init__(self, msg):
        super().__init__(msg);
class WaterError(Garden):
    def __init__(self, msg):
        super().__init__(msg);
class HealthError(Garden):
    def __init__(self, msg):
        super().__init__(msg);

class GardenManager:
    def __init__(self, names, water_level, sunlight_hours):
        self._plants = {}
        self.add_plant(names, water_level, sunlight_hours)
    def add_plant(self, names, water_level, sunlight_hours):
        for name in names:          
            if name  is None or name == "":
             raise PlantError(f"Rrror adding Planat: Plante name cannot be empty or None");
            self._plants[name] = {'_water_level':water_level, '_sunlight_hours' : sunlight_hours} 
    def water_plants(self):
        for name, value in self._plants.items():
            val = value.get('_water_level');
            if val is None or val < 1:
                raise WaterError(f"Error: Water level {val} to hight(min 1)") 
            elif val > 10:
                raise WaterError(f"Error: Water level {val} to hight(max 10)") 
            print(f"watering {name} = success")
    def check_health(self):
        for key, value in self._plants.items():
            val = value.get('_sunlight_hours');
            if val is None or val< 2:
                raise HealthError(f"Error sunlight {val} is too low(min 2)") 
            elif val > 12:
                raise HealthError(f"Error sunlight {val} is too high (max 12)") 
            print(f"{key} (water: {value.get('_water_level')} sun: {value})")

def test_garden(): 
    manager = GardenManager(["ana"], 9, 11)
    print("=== NORMAL CASE ===")
    try:
        manager.add_plant(["tomato"], 10, 5)
        manager.add_plant(["lettuce"], 1, 2)
        manager.water_plants()
        manager.check_health()
        print("Garden working normally")
    except Garden as e:
        print("Error:", e)
    finally:
        print("Cleaning up garden system")

    print("\n=== ERROR CASE ===")
    try:
        manager.add_plant([""], 10, 5)
        manager.add_plant(["lettuce"], 1, 15)
        manager.water_plants()  # cactus does not exist
    except PlantError as e:
        print("PlantError:", e)
    except Garden as e:
        print("GardenError:", e)
    finally:
        print("Cleaning up garden system")

    print("\n=== SYSTEM STILL RUNNING ===")
    try:
        manager.water_plants()
        print("Garden still works after error")
    except Garden as e:
        print("Error:", e)
    finally:
        print("Final cleanup")

if __name__== "__main__":
   print("=== Graden Management System"); 
   test_garden();
   print("Graden management systen test complete'")
