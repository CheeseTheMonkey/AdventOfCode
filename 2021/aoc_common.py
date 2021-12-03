def read_file_by_line(filename):
    return open(filename).read().rstrip('\n').split('\n')

def read_file_by_int(filename):
    return [int(a) for a in read_file_by_line(filename)]
