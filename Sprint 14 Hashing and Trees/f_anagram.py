_ = int(input())
s = [tuple(sorted(list(x))) for x in input().split()]
d = dict()
for i in range(len(s)):
    d[s[i]] = d.get(s[i], '') + str(i) + ' '


print(*d.values(), sep='\n')
