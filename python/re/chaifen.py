import re


def main():
    poem = '东风夜放花千树。更吹落，星如雨。宝马雕车香满路。凤箫声动，玉壶光转，一夜鱼龙舞。\
蛾儿雪柳黄金缕。笑语盈盈暗香去。众里寻他千百度。蓦然回首，那人却在，灯火阑珊处。'
    sentence_list = re.split(r'[,.，。]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == "__main__":
    main()
