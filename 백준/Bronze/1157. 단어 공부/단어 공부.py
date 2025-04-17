w = input().strip().upper()
c = [0] * 26

for x in w:
    c[ord(x) - ord('A')] += 1

m = max(c)
if c.count(m) > 1:
    print('?')
else:
    print(chr(c.index(m) + ord('A')))