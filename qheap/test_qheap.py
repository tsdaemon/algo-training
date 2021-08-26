from qheap.qheap import Heap

INPUT_FILE = 'qheap/test_input.txt'
EXPECTED_OUTPUT_FILE = 'qheap/test_output.txt'


def read_file(name):
    with open(name, 'r') as f:
        lines = f.readlines()

    return lines


def test_heap():
    test_input = read_file(INPUT_FILE)
    h = Heap()
    actual_ouput = []
    for command in test_input[1:]:
        action = command.split()
        operation = int(action[0])
        if operation == 1:
            h.insert(int(action[1]))
        elif operation == 2:
            h.delete(int(action[1]))
        else:
            actual_ouput.append(h.top())

    expected_output = list(map(int, read_file(EXPECTED_OUTPUT_FILE)))
    for i in range(len(expected_output)):
        assert expected_output[i] == actual_ouput[i], f'Difference at line {i}'
