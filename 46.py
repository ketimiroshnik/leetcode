# 200. Number of Islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        def recur(i, j, num):
            grid[i][j] = num
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x > n:
                    continue
                if y < 0 or y > m:
                    continue
                if grid[x][y] == "1":
                    recur(x, y, num)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    recur(i, j, count)
        return count



