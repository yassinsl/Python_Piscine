from sys import exit
from time import perf_counter
import random

def print_total(total, high_level, treasure, level_up):
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

def process_stream(iterator):
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    start = perf_counter()
    try:
        while True:
            it = next(iterator)
            total += 1

            if it["level"] >= 10:
                high_level += 1
            if it["type"] == "treasure":
                treasure += 1
            if it["type"] == "level_up":
                level_up += 1
    except StopIteration:
        pass

    end = perf_counter()
    print_total(total, high_level, treasure, level_up)
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {(end - start):.3f} seconds")

def generate_game_events(number):
    players = ["alice", "bob", "charlie", "dina", "yassine", "meryem"]
    types = ["kill", "treasure", "level_up"]

    for i in range(1, number + 1):
        player = random.choice(players)
        level = random.randint(1, 20)
        type_name = random.choice(types)

        if type_name == "kill":
            details = {"target": "monster"}
        elif type_name == "treasure":
            details = {"item": "gold", "amount": 50}
        else:  # level_up
            details = {"from": level - 1, "to": level}

        yield {
            "id": i,
            "player": player,
            "level": level,
            "type": type_name,
            "details": details,
        }

def print_events(iterator, num_to_print):
    print(f"Processing {num_to_print} sample events...")
    for _ in range(num_to_print):
        try:
            ev = next(iterator)
        except StopIteration:
            return

        if ev["type"] == "kill":
            print(f"Event {ev['id']}: Player {ev['player']} (level {ev['level']}) killed {ev['details']['target']}")
        elif ev["type"] == "treasure":
            print(f"Event {ev['id']}: Player {ev['player']} (level {ev['level']}) found treasure")
        else:
            print(f"Event {ev['id']}: Player {ev['player']} (level {ev['level']}) leveled up")

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    try:
        input_number = int(input("Enter number of events to generate: "))
    except ValueError:
        print("Error: please enter a valid integer.")
        exit(1)

    if input_number <= 0:
        print("Error: number must be > 0.")
        exit(1)

    stream = generate_game_events(input_number)
    print_events(stream, 3)
    process_stream(stream)

