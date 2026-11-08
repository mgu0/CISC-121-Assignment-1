def solution(a, k):
    # preforms the rotation k times
    for i in range(k):
        # remove and save the last item into a variable
        last = a.pop()

        # insert the item in the beginning
        a.insert(0, last)

    # return the finished fully rotated array
    return a