if __name__== "__main__":
    print("=== CYBER ARCHRVES PRESERVATION ===");
    data =[ "{[}ENTRY 001{]} New quantum algorithm discovered\n", "{[}ENTRY 002{]} Efficiency increased by 347%\n","{[}ENTRY 003{]} Archived by Data Archivist trainee]:\n"]
    try:
        with open("new_discovery.txt", "w") as f:
            print(f"Inetializing new storage unit: {f.name}")
            for dt in data:
                f.write(dt);
        print("Storage unit created sucessfully...")
    except PermissionError :
           print("Error : PErmission Dinied")
    try:
        with open("new_discovery.txt", "r") as f:
            print(f"Inscribing presergation data...")
            datas = f.read()
            print(datas);
        print("Data inscription complete stroage unit trainee")
    except PermissionError :
           print("Error : PErmission Dinied")

