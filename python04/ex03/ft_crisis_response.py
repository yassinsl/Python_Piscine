from  sys import exit
if __name__ == "__main__":
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===")
    file_name = input("Please Enter the file name to open: ");
    if file_name == "":
        exit(1);
    print(f"CRISIS ALERT: Attempting access to '{file_name}'")
    try:
        with open(file_name, "r") as f:
            data = f.read();
            print(f"REPONSE: Archive recovered ``{data}``")
            print("STATUS: Normal  operations resumed ")
    except FileNotFoundError as e:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled system stable")
    except PermissionError as e:
        print("RESPONSE: Security protocls deny access")
        print("STATUS: Crisis handled , sexurity maintained") 
    finally:
        print("All crisi scenatios handle successfully. Archives seure.")
        
