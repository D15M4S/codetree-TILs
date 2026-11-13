n = int(input())


for i in range(1, n + 1):
    flag = True
    if i % 3 == 0:
        print(0, end=' ')
        flag = False
        continue
    
    lst = [3, 6, 9]
    k = i
    for _ in range(len(str(i))):
        if k % 10 in lst:
            print(0, end=' ')
            flag = False
            break
        k //= 10

    if flag == True:        
        print(i, end=' ')

