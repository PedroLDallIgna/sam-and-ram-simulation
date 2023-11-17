import sys
import time
import random

def main(file):
    print(f'========== {file} ==========')

    sam = []
    ram = []

    with open(file, "r") as f:
        for line in f.readlines():
            sam.append(line.replace('\n', ''))
            ram.append(line.replace('\n', ''))

            random.shuffle(ram)

    while info := input("Word: "):
        search_sam(sam, info)
        search_ram(ram, info)
        print()


def search_sam(memory, info):
    start = time.time_ns() / 1000000
    for row in memory:
        if (row == info):
            break
    finish = time.time_ns() / 1000000

    print("SAM time: %fms" % (finish - start))


def search_ram(memory, info):
    start = time.time_ns() / 1000000
    addresses = [i for i in range(0, len(memory))]
    random_address = random.choice(addresses)
    addresses.remove(random_address)
    while not memory[random_address] == info:
        random_address = random.choice(addresses)
        addresses.remove(random_address)

    finish = time.time_ns() / 1000000
    print("RAM time: %fms" % (finish - start))


if __name__ == "__main__":
    main(sys.argv[1])