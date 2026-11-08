def solution(a):
    # sort the list in ascending order
    a.sort()
    # a tracker variable, and set it equal to 1
    expected = 1

    # for loop for every element in the sorted list
    for i in a:
        # if the current element is not equal to the expected element, that means it is not a permutation, return 0
        if i != expected:
            return 0
        # increment expected by 1 to get ready for the next pass
        expected += 1
    # if the for loop passes fully successfully, that means the list is a permutation, return 1
    return 1