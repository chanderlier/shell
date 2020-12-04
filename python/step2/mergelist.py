def merge(items1, items2, comp=lambda x, y: x < y):
    '''合并（将两个有序的列表合并成一个有序的列表'''
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1],items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


if __name__ == "__main__":
    items1 = [1, 3, 5, 6, 7, 8]
    items2 = [2, 4, 7, 9, 10]
    items = [1, 42, 423, 534, 344, 4434, 222, 123, 45, 3]
    '''list1 = _merge_sort(items1)
    list2 = _merge_sort(items2)
    '''
    # 将两个有序列表items1，items2有序合并后的结果打印出来
    print(merge(items1,items2))
    # print(merge_sort(items1))
    # 将items归并排序的结果打印出来
    print(_merge_sort(items,comp=lambda x, y: x < y))