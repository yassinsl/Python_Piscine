if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    content = [
        "New security protocols archived\n",
        "Vault automatically sealed upon completion\n",
    ]

    try:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols")

        with open("Archevies.txt", "r+") as file:
            print("SECURE EXTRACTION:")
            for line in file:
                line = line.rstrip("\n")
                if line:
                    print(f"{{[}}CLASSIFIED{{]}} {line}")
            file.seek(0, 2) 
            print("SECURE PRESERVATION:")
            for cn in content:
                file.write(cn)
                print(f"{{[}}CLASSIFIED{{]}} {cn.rstrip()}")

    except FileNotFoundError:
        print("RESPONSE: Archive missing")
        print("STATUS: System stable")

    except PermissionError:
        print("RESPONSE: Security denied")
        print("STATUS: Security maintained")

    finally:
        print("All vault operations completed with maximum security")

