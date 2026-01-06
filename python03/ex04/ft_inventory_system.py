if __name__ == "__main__":
    print("=== Player Inventory System ===")
    Inventory = {
      "alice" :{
            "sword":{
                "quantities":1,
                "type":("weapon, rare"),
                "value":500,
                },
            "potion":{
                "quantities":5,
                "type": ["consumble", "common"],
                "value": 50
                },
            "shield":{
                "quantities" : 1,
                "type": ["armor", "uncomman"],
                "value": 200
                }
            }
            }
    print("=== Alice's Inventory=== ")
    sword_alice = Inventory['alice'].get("sword");
    potion_alice = Inventory['alice'].get("potion");
    shield_alice = Inventory['alice'].get("shield");
    print(f"")

