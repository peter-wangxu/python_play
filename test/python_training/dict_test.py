f = open(r'C:\Users\wangp11\test.txt', 'r')

lines = 0
words = 0
chars = 0
diff = {}
diff_set = set()
for line in f:
    ws = line.split()
    lines += 1
    words += len(ws)
    chars += len(line)
    diff_set.update(ws)
    for word in ws:
        diff[word] = diff.get(word, 0) + 1


print lines
print words
print chars
print len(diff)
print len(diff_set)