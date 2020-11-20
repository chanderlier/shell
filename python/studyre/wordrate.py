import re
strip_str = '.(),:";->=\'\\+'
functionalwords = ["and", "for", "the", "of", "with", "by", "we", "it"]
with open('studypython/studyre/test.txt') as f:
    file = f.read()
    for ch in strip_str:
        file = file.replace(ch, ' ')
    words = [word for word in file.split() if re.findall(r'\w', word)]
sums = len(words)
s1 = []

for i in words:
    if i not in functionalwords:
        s1.append(i)
words = s1
number = len(words)
rate = number / sums
print(rate)
