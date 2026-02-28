# Date: 28/02/2026 (Saturday)

# 1.
'''
l = ["p1.py", "first.txt", "T3.py","Tk.txt","TFK.com"]
d = {}
for s in l:
    temp = s.split('.')
    if temp[1] not in d:
        d[temp[1]] = [temp[0]]
    else:
        d[temp[1]].append(temp[0])
    
print(d)
'''

# 2.
s = 'aaabbaabcc'
prev = s[0]
ans = s[0]
count = 0
for i in s:
    if i == prev:
        count+=1
    else:
        ans += str(count)
        ans += i
        count = 1
    prev = i
ans += str(count)
print(ans)