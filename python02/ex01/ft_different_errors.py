def garden_operation(mode):
    if mode == 'value':
        int("abc");
    elif mode == 'zero':        
        num = 5/0;
    elif mode == 'file':
        file = open('filea', 'r');
    elif mode == 'key' :
        der = {'name' : 'yassin', 'age' : 3};
        my = der.get('nn', 'a')
def test_error_types():
    print('Testing ValueError...')
    try:
        garden_operation("value");
    except  ValueError:
        print('Caught ValueError: invalid literal for int()');
    print('Testing ZeroDivisionError...')
    try:
        garden_operation("zero");
    except  ZeroDivisionError:
        print('Caught ZeroDivisionError: division by zero');
    print('Testing FileNotFoundError ...')
    try:
        garden_operation("file");
    except  FileNotFoundError:
        print('Caught FileNotFoundError: No such file "file.txt"');
    print('Test KeyError...')
    try:
        garden_operation("key");
    except  KeyError:
        print('Caught KeyError: division by zero');
    print('Caught multiple errors together ');
    try:
        garden_operation("value");
    except (KeyError, ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues");
    print("All error types tested sccessfully");
if __name__ == "__main__":
    test_error_types();
