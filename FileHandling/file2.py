# With statement

try:
    with open('auto.txt', mode='r') as file:
        print(file.read())
except FileNotFoundError as err:
    print(f'File does not exist')
    raise err
except IOError as err:
    print(f'IO error occurred')
    raise err
