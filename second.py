
def safe_rows(filename):
    with open (filename, 'r') as file:
        rows = [list(map(int, line.split())) for line in file]
    
    
    saferows = 0
    unsaferows = []
    for row in rows:
        safecheck = 0
        for i in range(len(row)):
            if i == (len(row) - 1):
                pass
            elif row[i] - row[i+1] <= 3 and row[i] - row[i+1] > 0:
                safecheck += 1
            elif row[i] - row[i+1] >= -3 and row[i] - row[i+1] < 0:
                safecheck -= 1
            else:
                pass
        if abs(safecheck) == (len(row)-1):
            saferows += 1
        else: 
            unsaferows += [row]
    return unsaferows

def p2_safe(list_unsafe):
    saferows = 0
    for row in list_unsafe:
        loopcheck = 0
        for i in range(len(row)):
            x = row.pop(i)
            safecheck = 0
            for n in range(len(row)):
                if n == (len(row) - 1):
                    pass
                elif row[n] - row[n+1] <= 3 and row[n] - row[n+1] > 0:
                    safecheck += 1
                elif row[n] - row[n+1] >= -3 and row[n] - row[n+1] < 0:
                    safecheck -= 1
                else:
                    pass
            
            if abs(safecheck) == len(row) - 1:
                loopcheck += 1
            row.insert(i, x)
        if loopcheck != 0:
            saferows += 1
                    
            
            
    print(saferows)






def main():
    p2_safe(safe_rows('day2_input.txt'))


if __name__ == '__main__':
    main()
