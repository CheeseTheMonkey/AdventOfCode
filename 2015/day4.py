
from hashlib import md5

def main():
    start = "iwrupvqb"
    i = 0
    while not md5(f'{start}{i}'.encode('utf8')).hexdigest().startswith("00000"):
        i += 1

    print(f"Part One: {i}")

    while not md5(f'{start}{i}'.encode('utf8')).hexdigest().startswith("000000"):
        i += 1

    print(f"Part Two: {i}")
    

if __name__ == '__main__':
    main()