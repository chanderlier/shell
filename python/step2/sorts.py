"""
def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = 1
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def main():
    lists = [123, 3242, 42423, 4234242, 4342, 233]
    print(select_sort(lists))


if __name__ == "__main__":
    main()
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
