import re
strip_str = '.(),:";->=\'\\+'
with open('studypython/studyre/test.txt') as f:
    file = f.read()
    for ch in strip_str:
        file = file.replace(ch, ' ')
    words = [word for word in file.split() if re.findall(r'\w', word)]

sums = len(words)
print(sums)
