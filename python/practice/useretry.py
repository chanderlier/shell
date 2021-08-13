from retry import retry
import datetime


start = datetime.datetime.now()
for i in range(100000):
    print(i)
end = datetime.datetime.now()
print((end - start).total_seconds())


def test():
    for i in range(10):
        try:
            print(i)
            if i == 8:
                print('yes')
                raise()
            else:
                print('error')
        except ValueError as e:
            print(e)


@retry()
def make_trouble():
    '''Retry until succeed'''
    print('retrying...')
    raise


# if __name__ == '__main__':
    # make_trouble()
    # test()
