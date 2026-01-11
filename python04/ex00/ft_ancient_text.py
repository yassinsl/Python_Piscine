if __name__== "__main__":
    print("====== CYBER ARCHIVES-DATA RECOVER SYSTEM ====")
    try:
        with open("ancient_fragment.txt", "r")as f:
            data = f.read();
        print(f"accessing Storage:{f.name}")
        print("Connection established");
        print()
        print("RECOVERED DATA:")
        print(data);
    except FileNotFoundError:
        print(f"file not found")
    except PermissionError:
        print(f"Permission Dinied")
    finally:
        print("Data recovery complete, Storage unit disconnected")
