def migratoryBirds(arr):
    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    value = 0
    key = 0

    for x, y in freq.items():
        if y > value or (y == value and x < key):
            value = y
            key = x

    return key
