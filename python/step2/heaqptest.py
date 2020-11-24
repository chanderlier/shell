import heapq
list1 = [23, 435, 543, 433, 34, 233, 555, 666, 888, 1024, 91]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.44},
    {'name': 'APPLE', 'shares': 300, 'price': 291.44},
    {'name': 'MS', 'shares': 60, 'price': 59.44},
    {'name': 'SOP', 'shares': 97, 'price': 311.45},
    {'name': 'AWS', 'shares': 80, 'price': 491.4},
    {'name': 'SINA', 'shares': 70, 'price': 193.32},
    {'name': 'HP', 'shares': 70, 'price': 69.32},
    {'name': 'YAHOO', 'shares': 70, 'price': 93.32},

]
# 输出list1最大大三个元素
print(heapq.nlargest(3, list1))
# 输出list1最小大三个元素
print(heapq.nsmallest(3, list1))
# 输出列表2，排位顺序price最高的两个元素
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# 输出列表2，按排位顺序，shares最小的两个元素,
print(heapq.nsmallest(2, list2, key=lambda x: x['shares']))
