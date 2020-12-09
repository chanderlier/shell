def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


if __name__ == "__main__":
    items = [12, 32, 44, 523, 3252, 5322, 5, 444]
    key = 44
    print(seq_search(items, key))