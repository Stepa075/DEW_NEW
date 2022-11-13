ls1 = [1, 2, 3, 4, 5, 6, 'hr']
ls2 = [9, 8, 'hr', 7, 6, 5]
vv = []
for lis in ls1:
    if lis not in ls2: ls2.append(lis)

print(ls2)
