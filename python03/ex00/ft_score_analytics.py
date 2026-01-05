import sys
def print_content(lst):
    print(f"scores processed: {lst}")
    print(f"Total player: {len(lst)}")
    print(f"Total score: {sum(lst)}")
    print(f"Average score: {sum(lst) / len(lst)}")
    print(f"High score: {max(lst)}")
    print(f"Low score: {min(lst)}")
    print(f"Score range: {max(lst) - min(lst)}")


if __name__== "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py  <score1> <score2> ...")
        exit(1)
    lst = [];
    for i in sys.argv[1:]:
        try:
            value = int(i);
            lst.append(value);
        except ValueError as e:
            print(e);
            exit(1)
    print_content(lst);
