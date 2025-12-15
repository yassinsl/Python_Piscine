def ft_count_harvest_recursive(number):
        if number == 0: 
                return 
        ft_count_harvest_recursive(number - 1)
        print("Day", number)
