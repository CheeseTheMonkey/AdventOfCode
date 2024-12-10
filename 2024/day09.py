from common import read_input
from copy import copy


def p1(file_system: list[int]):
    last_file_value = len(file_system) // 2
    file_system_without_space_reversed = [a for a in file_system[len(file_system)-1::-2]]
    compressed_file_system = []
    final_size_on_disk = sum(file_system[0::2])
    current_index = 0
    current_file = 0
    position_on_disk = 0
    while position_on_disk < final_size_on_disk:
        if current_index % 2:
            count = file_system[current_index]
            for _ in range(count):
                if not file_system_without_space_reversed[0]:
                    del file_system_without_space_reversed[0]
                    last_file_value -= 1
                position_on_disk += 1
                file_system_without_space_reversed[0] -= 1
                compressed_file_system.append(last_file_value)

        else:
            for i in range(file_system[current_index]):
                position_on_disk += 1
                compressed_file_system.append(current_file)
            current_file += 1

        # print("".join(str(a) for a in compressed_file_system[:final_size_on_disk]))
        current_index += 1
    print(f"Part One: {sum(i*a for i,a in enumerate(compressed_file_system[:final_size_on_disk]))}")

def day09():
    file_system = read_input(9)[0]
    p1([int(a) for a in file_system])


if __name__ == "__main__":
    day09()