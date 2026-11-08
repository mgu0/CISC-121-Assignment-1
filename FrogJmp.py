def solution(x, y ,d):
    # if the start and the end is that the same place no jumps are needed
    if x == y:
        return 0

    # calculate the distance between the start and the end
    difference = y - x

    # do floor division on the difference with the distance for each jump, calculates theoretically the least amount of jumps required
    jumps = difference // d

    # if the number of theoretical jumps is too small, add 1 jump
    if (jumps * d) + x < y:
        jumps += 1

    # returns the number of jumps required
    return jumps