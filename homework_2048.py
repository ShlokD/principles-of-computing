'''
Module for implementing 2048 merge
'''
def seperate_zeroes(input_list):
    '''
    Moves non zeroes to one side of the list and zeroes to another side
    :param inputList: list
    :return: list
    '''
    output_list = []
    zero_count = 0

    for counter in range(0, len(input_list)):
        if input_list[counter] == 0:
            zero_count += 1
        else:
            output_list.append(input_list[counter])

    return output_list + [0] * zero_count

def merge(line):
    """

    :param line: list of integers
    :return: merged array
    """

    list_a = seperate_zeroes(line)
    list_b = []

    index_a = 0
    while index_a < len(list_a):
        if index_a + 1 < len(list_a) and list_a[index_a] == list_a[index_a + 1]:
            list_b.append(2 * list_a[index_a])
            list_b.append(0)
            index_a += 2
        else:
            list_b.append(list_a[index_a])
            index_a += 1

    return seperate_zeroes(list_b)

