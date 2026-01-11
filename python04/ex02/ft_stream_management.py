from sys import stdin, stdout, stderr, exit

def take_input():
    stdout.write("Enter archive ID: ")
    stdout.flush()
    archive_id = stdin.readline().strip()

    if not archive_id or not archive_id.startswith("ARCH_"):
        stderr.write("Error: ID must start with ARCH_\n")
        exit(1)
    suffix = archive_id[len("ARCH_"):]
    if (ch.isdigit() for ch in suffix):
        stderr.write("Error: archive_id must NOT contain numbers\n")
        exit(1)
    stdout.write("Enter status report: ")
    stdout.flush()
    status = stdin.readline().strip()

    if not status:
        stderr.write("Error: Please enter a non-empty status\n")
        exit(1)
    # Print with your weird "{[}" and "{]}" style:
    stdout.write(f"\"{{[}}STANDARD{{]}}\" Archive status from {archive_id} : {status}\n")
    stdout.write("{[}ALERT{]} System diagnostic: communication channels verified\n")
    stdout.write("{[}STANDARD{]} Data transmission complete\n")

if __name__ == "__main__":
    print("==== CYBER ARCHIVES - COMMUNICATION SYSTEM ====")
    print()
    take_input()
    print("Inter-channel communication test successful")

