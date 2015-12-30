'''
combining mine and the borrowed

Created on 30 Dec 2015

@author: chris
'''
#!/usr/bin/py
# def matchSubArray(arr, pat, x, y, pat_y, pat_x):
#     for running_y in xrange(pat_y):
#         for running_x in xrange(pat_x):
#             if arr[running_y+y][running_x+x] != pat[running_y][running_x]:
#                 return False
#      
#     return True
             
             
def solveBruteForce(grid, patt, arr_y, arr_x, pat_y, pat_x):
    
    pattFirstRow = patt[0]
    firstCoords = []
    for i, gridRow in enumerate(grid[:-len(patt)+1]):
        try:
            startColSearch = 0
            while True:
                colStart = gridRow.index(pattFirstRow, startColSearch)
                firstCoords.append([i,colStart])
                startColSearch = colStart + 1
            
        except(ValueError):
            pass
    
    # From these coords, checking the rest of the pattern matches
    
    found = False
    for row, col in firstCoords:
        for j, pattRow in enumerate(patt[1:]):
            addRow = j + 1
            found = grid[row + addRow][col : col + len(pattRow)] == pattRow
            if not found:
                break
        if found:
            return True
    
    return False
     
if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        arr_y, arr_x = map(int, raw_input().split())
        arr = [0] * arr_y
        for y in xrange(arr_y):
            arr[y] = list(raw_input())
         
        pat_y, pat_x = map(int, raw_input().split())
        pat = [0] * pat_y
        for y in xrange(pat_y):
            pat[y] = list(raw_input())
         
        if solveBruteForce(arr, pat, arr_y, arr_x, pat_y, pat_x):
            print "YES"
        else:
            print "NO"