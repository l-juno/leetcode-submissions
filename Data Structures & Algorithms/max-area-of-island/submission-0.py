class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(x, y):
            currArea = 1
            if (x, y) in visited:
                return 0
            visited.add((x, y))
            for direction in directions:
                newX = x+direction[0]
                newY = y+direction[1]
                if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]):
                    continue
                if grid[newX][newY] == 0:
                    continue
                else:
                    currArea += dfs(newX, newY)
            return currArea
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
                    currArea = 0
        
        return maxArea