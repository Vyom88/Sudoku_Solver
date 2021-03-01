#checks the smae row
def checkItsRow(arr, lisnine, posr, posc):
    for i in range(9):
        if arr[posr][i] in lisnine:
            lisnine.remove(arr[posr][i])
            if lisnine.__len__() == 0:
                return lisnine
    return lisnine

#checks the same column
def checkItsCol(arr, lisnine, posr, posc):
    for i in range(9):
        if arr[i][posc] in lisnine:
            lisnine.remove(arr[i][posc])
            if lisnine.__len__() == 0:
                return lisnine
    return lisnine

#checks above and below row
def checkRow(arr, lisnine, posr, posc, dic, rownum):
    rowChecking = -1
    if rownum == 1:
        if (posr+1) % 3 == 1:
            rowChecking = posr + 1
        elif (posr+1) % 3 == 2:
            rowChecking = posr - 1
        elif (posr+1) % 3 == 0:
            rowChecking = posr - 2

        for i in range(9):
            if i+1 in arr[rowChecking]:
                if i+1 in lisnine:
                    #dic = [row1, row2, col1, col2]
                    dic[i+1][0] = True
    
    elif rownum == 2:
        if (posr+1) % 3 == 1:
            rowChecking = posr + 2
        elif (posr+1) % 3 == 2:
            rowChecking = posr + 1
        elif (posr+1) % 3 == 0:
            rowChecking = posr - 1

        for i in range(9):
            if i+1 in arr[rowChecking]:
                if i+1 in lisnine:
                    #dic = [row1, row2, col1, col2]
                    dic[i+1][1] = True
    
    return dic

#checks above and below cols
def checkCol(arr, lisnine, posr, posc, dic, colnum):
    colChecking = -1
    if colnum == 1:
        if (posc+1) % 3 == 1:
            colChecking = posc + 1
        elif (posc+1) % 3 == 2:
            colChecking = posc - 1
        elif (posc+1) % 3 == 0:
            colChecking = posc - 2
        
        for i in range(9):
            if i+1 in [row[colChecking] for row in arr]:
                if i+1 in lisnine:
                    #dic = [row1, row2, col1, col2]
                    dic[i+1][2] = True
    
    elif colnum == 2:
        if (posc+1) % 3 == 1:
            colChecking = posc + 2
        elif (posc+1) % 3 == 2:
            colChecking = posc + 1
        elif (posc+1) % 3 == 0:
            colChecking = posc - 1

        for i in range(9):
            if i+1 in [row[colChecking] for row in arr]:
                if i+1 in lisnine:
                    #dic = [row1, row2, col1, col2]
                    dic[i+1][3] = True

    return dic

#finds out which block it is in
def block1(arr, lisnine, posr, posc):
    block = 0
    if posr < 3:
        if posc < 3:
            block = 1
        elif posc > 2 and posc < 6:
            block = 2
        elif posc > 5 and posc < 9:
            block = 3
    
    elif posr > 2 and posr < 6:
        if posc < 3:
            block = 4
        elif posc > 2 and posc < 6:
            block = 5
        elif posc > 5 and posc < 9:
            block = 6
    
    elif posr > 5 and posr < 9:
        if posc < 3:
            block = 7
        elif posc > 2 and posc < 6:
            block = 8
        elif posc > 5 and posc < 9:
            block = 9
    
    return block

#checks for same num in block
def blockCal(arr, lisnine, posr, posc, block):
    if block == 1:
        for i in range(3):
            for j in range(3):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
    
    elif block == 2:
        for i in range(3):
            for j in range(3, 6):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
    
    elif block == 3:
        for i in range(3):
            for j in range(6, 9):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
    
    elif block == 4:
        for i in range(3, 6):
            for j in range(3):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
    
    elif block == 5:
        for i in range(3, 6):
            for j in range(3, 6):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
                
    elif block == 6:
        for i in range(3, 6):
            for j in range(6, 9):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
    
    elif block == 7:
        for i in range(6, 9):
            for j in range(3):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])
    
    elif block == 8:
        for i in range(6, 9):
            for j in range(3, 6):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])

    elif block == 9:
        for i in range(6, 9):
            for j in range(6, 9):
                if arr[i][j] in lisnine:
                    lisnine.remove(arr[i][j])

    return lisnine

#calculates things from the dic
def calc(arr, lisnine, posr, posc, dic, block):
    if lisnine.__len__() == 0:
        return -1
    
    else:
        lisninereal = []
        posrr = 0
        poscc = 0
        if (posc+1) % 3 == 1:
            poscc = 0
        elif (posc+1) % 3 == 2:
            poscc = 1
        elif (posc+1) % 3 == 0:
            poscc = 2
        
        if (posr+1) % 3 == 1:
            posrr = 0
        elif (posr+1) % 3 == 2:
            posrr = 1
        elif (posr+1) % 3 == 0:
            posrr = 2

        for i in range(lisnine.__len__()):
            rows = []
            cols = []
            templis = []

            if dic[lisnine[i]] == [True, True, True, True]:
                lisninereal.append(lisnine[i])
                continue

            if dic[lisnine[i]][0] == False:
                #dic = [row1, row2, col1, col2]
                tempr = 0
                tempc = posc
                
                if posrr == 0:
                    tempr = posr + 1
                elif posrr == 1:
                    tempr = posr - 1
                elif posrr == 2:
                    tempr = posr - 2
                if arr[tempr][tempc] == 0:
                    templis = checkItsRow(arr, [lisnine[i]], tempr, tempc)
                    if templis == [lisnine[i]]:
                        continue
                    rows.append(tempr)
                    
            
            if dic[lisnine[i]][1] == False:
                #dic = [row1, row2, col1, col2]
                tempr = 0
                tempc = posc
                
                if posrr == 0:
                    tempr = posr + 2
                elif posrr == 1:
                    tempr = posr + 1
                elif posrr == 2:
                    tempr = posr - 1

                if arr[tempr][tempc] == 0:
                    templis = checkItsRow(arr, [lisnine[i]], tempr, tempc)
                    if templis == [lisnine[i]]:
                        continue
                    rows.append(tempr)

            if dic[lisnine[i]][2] == False:
                #dic = [row1, row2, col1, col2]
                tempr = posr
                tempc = 0
                
                if poscc == 0:
                    tempc = posc + 1
                elif poscc == 1:
                    tempc = posc - 1
                elif poscc == 2:
                    tempc = posc - 2

                if arr[tempr][tempc] == 0:
                    templis = checkItsCol(arr, [lisnine[i]], tempr, tempc)
                    if templis == [lisnine[i]]:
                        continue
                    cols.append(tempc)

            if dic[lisnine[i]][3] == False:
                #dic = [row1, row2, col1, col2]
                tempr = posr
                tempc = 0
                
                if poscc == 0:
                    tempc = posc + 2
                elif poscc == 1:
                    tempc = posc + 1
                elif poscc == 2:
                    tempc = posc - 1

                if arr[tempr][tempc] == 0:
                    templis = checkItsCol(arr, [lisnine[i]], tempr, tempc)
                    if templis == [lisnine[i]]:
                        continue
                    cols.append(tempc)


            for x in rows:
                for y in cols:
                    if arr[x][y] == 0:
                        templis = checkItsCol(arr, [lisnine[i]], x, y)
                        templis = checkItsRow(arr, [lisnine[i]], x, y)
                        if templis == [lisnine[i]]:
                            continue

            lisninereal.append(lisnine[i])
        
        if lisninereal.__len__() == 0:
            return -1
        else:
            return lisninereal

def checkListFor(arr):
    bool = False
    for x in arr:
        for y in x:
            if y == 0:
                bool = True
                break
        
        if bool == True:
            break
    
    return bool

arr = []
file_object = open(r"C:\Vyom\Coding\Projects\test.txt","r")
for i in range(9):
    arr.append(list(map(int, file_object.readline().split(" "))))

impossible = False
while checkListFor(arr):
    for x in range(9):
        for y in range(9):
            if arr[x][y] == 0:
                lisnine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                lisnine = checkItsRow(arr, lisnine, x, y)
                lisnine = checkItsCol(arr, lisnine, x, y)
                block = block1(arr, lisnine, x, y)
                lisnine = blockCal(arr, lisnine, x, y, block)

                if lisnine.__len__() == 0:
                    impossible = True
                    break
                    
                dic = {}
                for z in lisnine:
                    dic[z] = [False, False, False, False]

                dic = checkRow(arr, lisnine, x, y, dic, 1)
                dic = checkRow(arr, lisnine, x, y, dic, 2)
                dic = checkCol(arr, lisnine, x, y, dic, 1)
                dic = checkCol(arr, lisnine, x, y, dic, 2)
            
                lisnine = calc(arr, lisnine, x, y, dic, block)
                if lisnine == -1:
                    continue
                elif lisnine.__len__() == 1:
                    arr[x][y] = lisnine[0]
                else:
                    continue
        
        if impossible == True:
            break

    if impossible == True:
        break

if impossible == True:
    print ("Impossible")

else:
    for x in arr:
        for y in x:
            print (str(y) + " ", end="")
        
        print ()