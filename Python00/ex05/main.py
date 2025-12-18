import ft_count_harvest_iterative as count_iterative
import ft_count_harvest_recursive as count_recursive

if __name__ == "__main__":
    number = int(input("Days until harvest: "))
    print("iterative is:")
    count_iterative.ft_count_harvest_iterative(number)
    print("recursive is:")
    count_recursive.ft_count_harvest_recursive(number)
