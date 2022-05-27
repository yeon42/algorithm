# 130

'''
mxn 크기의 이진 grid - 1(land), 0(water)
- 리턴: island의 수

* island
- 0으로 surround, 연결된 육지.
'''

class Solution(object):
    def numIslands(self, grid):

        row = len(grid)
        col = len(grid[0])
        island = 0

        def dfs(x, y):
            if 0<=x<row and 0<=y<col and grid[x][y] == '1':
                grid[x][y] = '0'

                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)

                return grid

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    print(dfs(i, j))
                    island += 1
        
        return island


'''
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]
'''

'''
  ["visited","visited","visited","visited", "0"],
  ["visited","visited",   "0",   "visited", "0"],
  ["visited","visited",   "0",      "0",    "0"],
  [   "0",      "0",      "0",      "0",    "0"]
'''

'''
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
'''

'''
  ["visited","visited","0","0","0"],
  ["visited","visited","0","0","0"],
  ["0","0","visited","0","0"],
  ["0","0","0","1","1"]
'''
