
from collections import Counter, deque


text = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
text = "bvwbjplbgvbhsrlpgdmjqwftvncz"
text ="nppdvjthqldpwncqszvftbrmjlhg"
text = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
text = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

text = open("day6.input").read().strip()

start_of_packet = 0
start_of_message = 0
packet_buff = deque(maxlen=4)
message_buff = deque(maxlen=14)

for idx, char in enumerate(text):
    if not start_of_packet and len(packet_buff) == 4:
        count = Counter(packet_buff)
        if max(count.values()) == 1:
            start_of_packet = idx
            
    if not start_of_message and len(message_buff) == 14:
        count = Counter(message_buff)
        if max(count.values()) == 1:
            start_of_message = idx
            break
    
    packet_buff.append(char)
    message_buff.append(char)

print(f"Part 1: {start_of_packet}")
print(f"Part 1: {start_of_message}")
