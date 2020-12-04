def select_sort(items, comp=lambda x, y: x < y):
    # 假设items = [1, 2, 4 ,3 ,7 ,6]
    items = items[:]
    # for i in range(6 -1)
    for i in range(len(items) - 1):
        # 最小索引设置为i
        min_index = i
        # for j in range(i + 1, 6)
        for j in range(i + 1, len(items)):
            # 比较items[j]和items[min_index]的大小
            if comp(items[j], items[min_index]):
                # 如果 items[j] < items[min_index],则将j赋值给min_index
                min_index = j
        # items[i], items[min_index]的值互换
        if i != min_index:
            items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == "__main__":
    list1 = [123, 345, 234, 343]
    # list1 = [123, 434, 222, 333, 233, 888, 1234565]
    print(select_sort(list1))


"""
def selectionSort(lists):
    for i in range(len(lists) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(lists)):
            if lists[j] < lists[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            lists[i], lists[minIndex] = lists[minIndex], lists[i]
    return lists


if __name__ == '__main__':
    list1 = list(map(int, input('请输入需要排序的数字: 用,隔开 ').split(",")))
    # list1 = [1, 5, 8, 3389, 54, 223, 3306, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list1)
    result = selectionSort(list1)
    print("List sort is:", result)
"""
