def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    n = len(array)
    end = n - 1
    begin = 0
    mid = (end + begin) // 2
    while end >= begin:
        mid_element = array[mid]
        if target == mid_element:
            return mid
        elif target > array[mid]:
            begin = mid + 1
            mid = int((end + begin)) // 2
        else:
            end = mid - 1
            mid = int((end + begin) // 2)
    return -1

def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
