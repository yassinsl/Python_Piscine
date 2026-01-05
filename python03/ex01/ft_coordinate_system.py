from math import sqrt
import sys

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    if len(sys.argv) != 2:
        print("Error: No position Usage: python3 ft_coordpnate_system \"(x,y,z)\"")
        exit(1);
    tup_00 = (10, 20, 5)
    tup_1 = (0, 0, 0)
    x1,y1,z1 = tup_1
    x0,y0,z0 = tup_00
    distance = sqrt((x0-x1)**2 + (y0-y1)**2 + (z0-z1)**2)
    print(f"position created: ({tup_00})")
    print(f"Distance between {tup_1} and {tup_00}: {distance}")
    lst = sys.argv[1].split(',')
    lst_num = []
    for i in lst:
        try:
            value = int(i)
            lst_num.append(value);
        except ValueError as e:
            print(f"Error Parsing coordinates: {e}");
            print(f"Error details - Type: ValueError, args:(\"{e}\")")
            exit(1);
    if len(lst_num) != 3:
        print("Error: expected exactly 3 numbers like: 1,2,3")
        exit(1);
    tup_2 = tuple(lst_num)
    x2,y2,z2 = tup_2;
    distance = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Parsing coordinates: {tup_2}");
    print(f"Distance between {tup_1} and {tup_2}: {distance}")
    print("Umpacking domomstrastion: ")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates at X={x2}, Y={y2}, Z={z2}")

