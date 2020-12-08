from bootcode import BootCode


data = open("day08.input").read().splitlines()


bc = BootCode()
print "Part 1: ", bc.run(data)[1]

mapping = {'jmp': 'nop', 'nop':'jmp'}

for i in range(len(data)):
    if data[i][:3] in mapping:
        new_data = list(data)
        new_data[i] = "{}{}".format(mapping[data[i][:3]], data[i][3:])
        completed, result = BootCode().run(new_data)
        if completed:
            print "Part 2: ", result
            break
