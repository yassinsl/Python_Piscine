def add_item(player_name, item, quantity, category, rarity, value):
    return {
        player_name: {
            item: {
                "quantity": quantity,
                "category": category,
                "rarity": rarity,
                "value": value
            }
        }
    }


def transfer_item(inventories, from_player):
    if from_player not in inventories:
        print("Player not found")
        return

    to_player = input("Enter the player to receive the item: ").strip()
    if to_player not in inventories:
        print("Receiver player not found")
        return

    item = input("Enter item name to transfer: ").strip()
    if item not in inventories[from_player]:
        print("Item not found in sender inventory")
        return

    qty = int(input("Enter quantity to transfer: "))
    if qty <= 0:
        print("Invalid quantity")
        return

    if inventories[from_player][item]["quantity"] < qty:
        print("Not enough quantity to transfer")
        return

    # remove from sender
    inventories[from_player][item]["quantity"] -= qty

    # add to receiver
    if item not in inventories[to_player]:
        inventories[to_player][item] = inventories[from_player][item].copy()
        inventories[to_player][item]["quantity"] = qty
    else:
        inventories[to_player][item]["quantity"] += qty

    # delete item if sender hits 0
    if inventories[from_player][item]["quantity"] == 0:
        del inventories[from_player][item]

    print("Transfer success.")


def category_summary(inventories, player):
    print("categories:", end=" ")
    seen = []
    for _, data in inventories[player].items():
        cat = data["category"]
        if cat not in seen:
            seen.append(cat)

    # print each category with total quantity in that category
    for i, cat in enumerate(seen):
        total = 0
        for _, data in inventories[player].items():
            if data["category"] == cat:
                total += data["quantity"]
        endc = ", " if i != len(seen) - 1 else ""
        print(f"{cat}({total})", end=endc)
    print()


def inventory_item_count(inventories, player):
    count = 0
    for _, data in inventories[player].items():
        count += data["quantity"]
    print(f"item count: {count}")


def inventory_total_value(values):
    total = 0
    for v in values:
        total += v
    print(f"Inventory total: {total} gold")


def print_inventory(inventories):
    player = input("Please enter the name of player: ").strip()

    if player not in inventories:
        print("Player not found")
        return

    values = []
    for item_name, data in inventories[player].items():
        item_total = data["quantity"] * data["value"]
        values.append(item_total)
        print(
            f"{item_name} ({data['category']}, {data['rarity']}): "
            f"{data['quantity']} x {data['value']} gold = {item_total} gold"
        )

    inventory_total_value(values)
    inventory_item_count(inventories, player)
    category_summary(inventories, player)

    do_transfer = input("Do you want to transfer an item? (y/n): ").strip().lower()
    if do_transfer == "y":
        transfer_item(inventories, player)


def take_data_from_user():
    inventories = {}

    for _ in range(3):
        player_name = input("Please enter the player name: ").strip()

        for _ in range(3):
            item = input("Please add item (sword/potion/shield): ").strip()
            quantity = int(input("Quantity: "))
            category = input("Category (weapon/consumable/armor): ").strip()
            rarity = input("Rarity (common/uncommon/rare/legendary): ").strip()
            value = int(input("Value (gold): "))

            one = add_item(player_name, item, quantity, category, rarity, value)

            if player_name not in inventories:
                inventories.update(one)
            else:
                inventories[player_name].update(one[player_name])

    return inventories


if __name__ == "__main__":
    print("=== Player Inventory System ===")
    inventories = take_data_from_user()
    print_inventory(inventories)

