class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(n):
            result.append([0] * n)
        for i in range(n):
            for j in range(n):
                # the k th circle
                k = min(i, j, n - i - 1, n - j - 1)
                # find the k th circle number
                start_index = 1
                for m in range(k):
                    start_index += 4 * (n - 2 * m - 1)
                # top
                if i == k:
                    result[i][j] = start_index + (j - k)

                # buttem
                elif n - i - 1 == k:
                    result[i][j] = start_index + 2 * ((n - 2 * k) - 1) + (n - 2 * k) - (j - k) - 1
                # left
                elif j == k:
                    result[i][j] = start_index + 3 * ((n - 2 * k) - 1) + (n - 2 * k) - (i - k) - 1
                # right
                elif n - j - 1 == k:
                    result[i][j] = start_index + (n - 2 * k) - 1 + i - k
        return result