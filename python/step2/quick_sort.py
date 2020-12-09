def quick_sort(items,  comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos -1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1 
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


if __name__ == "__main__":
    items = [12, 423243, 543, 435, 3534, 53, 53, 45, 34, 5, 35, 3, 45, 345, 345, 34, 5, 34, 5, 345, 345, 34, 53, 45, 34, 53, 45, 2, 3, 5555, 324243242342]
    print(quick_sort(items))