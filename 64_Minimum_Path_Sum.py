class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1 or len(grid[0]) == 1:
            return sum(list(map(sum,grid)))
        else:
            result = grid
            sum_grid = sum(list(map(sum,grid)))
            for _m in range(len(grid)):
                for _n in range(len(grid[0])):
                    if _m != 0 or _n != 0:
                        left = sum_grid
                        if _n > 0:
                            left = result[_m][_n - 1]
                        up = sum_grid
                        if _m > 0:
                            up = result[_m - 1][_n]
                        result[_m][_n] = min(left,up) + result[_m][_n]
            return result[-1][-1]