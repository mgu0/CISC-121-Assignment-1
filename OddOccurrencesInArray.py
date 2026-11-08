def solution(a):
    # define empty set
    unpaired = set()

    # loops through all the elements in list a
    for number in a:
        # if current number is already in the set, that means that its already paired so it gets removed
        if number in unpaired:
            unpaired.remove(number)
        else:
            # if the current number is not in the set it gets added to the set
            unpaired.add(number)

    # returns the last (and only) element in the set, which is the unpaired number
    return unpaired.pop()