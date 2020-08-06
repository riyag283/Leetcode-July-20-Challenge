def func(cells,N):
    val0, val1, val2, val3, val4, val5, val6, val7 = 0,0,0,0,0,0,0,0
    for i in range(N):
        if cells[0] == 1:
            val0 = 0
        if (cells[0] ^ cells[2] == 0):
            val1 = 1
        else:
            val1 = 0
        if (cells[1] ^ cells[3] == 0):
            val2 = 1
        else:
            val2 = 0
        if (cells[2] ^ cells[4] == 0):
            val3 = 1
        else:
            val3 = 0
        if (cells[3] ^ cells[5] == 0):
            val4 = 1
        else:
            val4 = 0
        if (cells[4] ^ cells[6] == 0):
            val5 = 1
        else:
            val5 = 0
        if (cells[5] ^ cells[7] == 0):
            val6 = 1
        else:
            val6 = 0
        if (cells[7] == 1):
            val7 = 0
        cells.clear()
        cells = [val0, val1, val2, val3, val4, val5, val6, val7]
        print(cells)
    return cells

cells = [0,1,0,1,1,0,0,1]
N = 7
print(func(cells,N))
