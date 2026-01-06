def Analytics_achivements(players):
    print("=== achivements Analytics ===")
    unique_achivements = players["alice"].union(players["bob"], players["charlie"])
    print(f"All unique achivements: {unique_achivements}");
    print(f"Total unique achivements: {len(unique_achivements)}")
    unique_achivements = players["alice"].intersection(players["bob"], players["charlie"])
    print(f"comman to all player: {unique_achivements}")

    print(f"Rare achivements (1player): {unique_achivements}")
    bob_unique = players["bob"].difference(
    players["alice"],
    players["charlie"]
    )
    alice_unique = players["alice"].difference(
    players["alice"],
    players["bob"]
    )
    charlie_unique = players["charlie"].difference(
    players["alice"],
    players["bob"]
    )
    rare_achievements = alice_unique | bob_unique | charlie_unique
    print(f"Rare achievements{rare_achievements}")
    ########################################################
    print(f"Alice vs Bob comman: {players['alice'].intersection(players['bob'])}")
    print(f"Alice unique: {players['alice'].difference(players['bob'])}")
    print(f"Bob unique: {players['bob'].difference(players['alice'])}")
def print_achivements(players):
    for player_name, achivements in players.items():
        print(f"player {player_name} achivements: {achivements}")
if __name__ == "__main__":
    print("=== Achievements Tracker System ===")
    players ={
            "alice":{"first_kill", "level_10", "treasure_hunter", "speed_demon"},
            "bob":{"first_kill", "level_10", "boss_slayer", "collector"},
            "charlie":{"level_10", "treasure_hunter", "boss_slayer", "perfectionist"}
            }
    print_achivements(players);
    Analytics_achivements(players);
