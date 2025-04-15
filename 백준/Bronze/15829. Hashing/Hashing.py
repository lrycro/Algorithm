length = int(input())
str = input()
r = 31
m = 1234567891
hash = 0

for i in range(length):
    cur = ord(str[i]) - 96
    hash += cur * (r ** i)

print(hash % m)