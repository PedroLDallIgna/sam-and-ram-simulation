import sys
import time
import random

def read_file(filename):
    with open(filename, "r") as file:
        arr = [line.strip() for line in file]

    return arr


def main(filename):
    sam = read_file(filename)
    ram = read_file(filename)
    random.shuffle(ram)

    while user_input := input(":").split():
        command = user_input[0]

        if (command == "search"):
            try:
                data = user_input[1]
            except:
                data = input("Data to search: ")

            print(f"Searching for: {data}")
            sequential_access_time = sequential_access(sam, data)
            print(f"Sequential Access Time: {sequential_access_time:.4f}ms")
            random_access_time = random_access(ram, data)
            print(f"Random Access Time: {random_access_time:.4f}ms")

            
            print()
        elif (command == "help"):
            help()
        elif (command == "quit"):
            break
        else:
            print("COMMAND NOT FOUND")
            help()
            continue

    return 0
            

def help():
    print("|- COMMANDS -------------------------|")
    print("|                                    |")
    print("| search <word>                      |")
    print("|    search for word in the memory.  |")
    print("|                                    |")
    print("| quit                               |")
    print("|    quit the program.               |")
    print("|                                    |")
    print("| help                               |")
    print("|    print this help.                |")
    print("|------------------------------------|")
    print()

def sequential_access(memory, info):
    start = time.time()
    for row in memory:
        if (row == info):
            break
    finish = time.time()

    return (finish - start) * 1000


def random_access(memory, info):
    address_table = [i for i in range(0, len(memory))]

    start = time.time()

    random_address = random.choice(address_table)
    address_table.remove(random_address)
    
    while not memory[random_address] == info:
        random_address = random.choice(address_table)
        address_table.remove(random_address)

    finish = time.time()

    return (finish - start) * 1000


if __name__ == "__main__":
    filename = sys.argv[1]
    print(f'============= {filename} =============')
    print()
    main(filename)