for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print('公鸡的数量为%d,母鸡的数量为%d,小鸡的数量为%d' % (x, y, z)) 