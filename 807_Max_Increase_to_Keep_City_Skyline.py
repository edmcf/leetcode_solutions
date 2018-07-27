class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        skyline_from_left = list(map(lambda x: max(x), grid))
        skyline_from_top = []
        for i in range(n):
            max_in_line = grid[0][i]
            for j in range(n):
                if grid[j][i] > max_in_line:
                    max_in_line = grid[j][i]
            skyline_from_top.append(max_in_line)
        result = 0
        for i in range(n):
            for j in range(n):
                result += min(skyline_from_top[j],skyline_from_left[i]) - grid[i][j]
        return result

print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,1]]))