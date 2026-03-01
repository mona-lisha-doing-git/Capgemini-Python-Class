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
'''
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
'''

# 3.
'''
l = ["Aditi", "Sarvesh", "Pradipt", "Bhavik"]
v = ""
for i in l:
    for j in i:
        if j in "aeiouAEIOU":
            v += j + ' '
print(v)
'''

# 4.
'''
l = [(2+3j), 12, 'Program', 'Python', False]
d = {}
for i in l:
    s = ''
    if type(i) == str:
        for j in i:
            if j in "aeiouAEIOU":
                s += j
        d[i] = s
print(d)
'''

# 5. break
# for i in range(1,11):
#     if(i == 5):
#         break
#     print(i)

# 6. continue
# for i in range(1,6):
#     if(i == 4):
#         continue
#     print(i)

# 7. pass
# for i in range(1,4):
#     for j in range(1,11):
#         pass
#     print(i)