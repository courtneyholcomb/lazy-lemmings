"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    farthest = 0

    for hole in range(num_holes):
        lowest_dist = num_holes - 1
        for cafe in cafes:
            dist = abs(hole - cafe)
            if dist < lowest_dist:
                lowest_dist = dist
        if lowest_dist > farthest:
            farthest = lowest_dist

    return farthest


def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    end = num_holes - 1
    farthest = 0

    for i in range(len(cafes)):
        # if first cafe, get distance to start
        if i == 0:
            dist = cafes[i] - 0
        # else get distance to last cafe, halved
        else:
            dist = (cafes[i] - cafes[i - 1]) // 2

        # if last cafe, get distance to end
        if i == len(cafes) - 1:
            end_dist = end - cafes[-1]
            if end_dist > dist:
                dist = end_dist
                
        if dist > farthest:
            farthest = dist

    return farthest


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
