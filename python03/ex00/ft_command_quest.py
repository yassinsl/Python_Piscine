import sys
def one_args(arg):
    print("No argemnt provided!")
    print(f"program name: {arg}")
    print("Total argument: 1")
    exit(1)
if __name__== "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        one_args(sys.argv[0]);
    print(f"program name: {sys.argv[0]}")
    print(f"argement received : {len(sys.argv) - 1}");
    i = 1;
    lst = []
    for lst in sys.argv[1:]:
        print(f"Argement {i}: {lst}")
        i+=1;
    print("Total arguments: {len(sys.argv)}")
