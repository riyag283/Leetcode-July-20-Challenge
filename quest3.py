'''def function(cells,n):
    for _ in range(N):
        temp = [0]
        for i in range(1,7):
            if cells[i-1]^cells[i+1]==1:
                temp.append(1)
            else:
                temp.append(0)
        temp.append(0)
        cells = temp
        print(cells)
    return cells
    '''

def func(cells,N):
    #print(cells)
    record = []
    x = 0
    for _ in range(N):
        list1 = [0,0,0,0,0,0,0,0]
        for i in range(1,7):
            if cells[i-1]^cells[i+1]==0:
                list1[i] = 1
            else:
                list1[i] = 0
        cells = list1
        x += 1
        if cells not in record:
            record.append(cells)
        else:
            break
    n = N%14
    print(record)
    print(n)
    return record[n-1]

    
cells = [0,0,0,1,1,0,1,0]
N = 574
print(func(cells,N))
