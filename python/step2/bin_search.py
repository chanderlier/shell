def bin_search(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    # items = [123, 42332, 5554, 333, 3332, 533]
    # key = 3332
    items = ['12', 'hello123', 'iam', 'kingslayer']
    key = 'kingslayer'
    print(bin_search(items, key))
