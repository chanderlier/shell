from datetime import datetime


def datecal(startdate, enddate):
    startdate = datetime.strptime(starttime, '%Y%m%d')
    enddate = datetime.strptime(endtime, '%Y%m%d')
    print(enddate - startdate)


if __name__ == "__main__":
    starttime = input('请输入起始日期: \n')
    endtime = input('请输入结束日期: \n')
    datecal(starttime, endtime)
