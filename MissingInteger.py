def solution(a):
    # default missing value of 1
    missing = 1

    # sorts the array ascending
    a.sort()

    # loops through every element in the array
    for i in a:
        # if the current value in the array is the same as the missing value, that means that its not missing
        if i == missing:
            # increment missing value by 1
            missing += 1
        # if previous condition was false, it checks if if the current value is greater than the missing value
        elif i > missing:
            # if this is the case, that means the missing value is indeed missing and terminates the for loop early
            break

    # returns the missing value
    return missing