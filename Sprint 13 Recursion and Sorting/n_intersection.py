n = int(input())
s = []
for i in range(n):
    seq = [int(x) for x in input().split()]
    s.append(seq)
s.sort()
for i in range(len(s)-1):
    if s[i+1][0] <= s[i][1]:
        tmp = s[i][1] < s[i+1][1]
        s[i+1][0] = s[i][0]
        s[i+1][1] = s[i+tmp][1]
        s[i] = []
for j in range(len(s)):
    if s[j]:
        print(*s[j])
