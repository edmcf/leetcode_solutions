class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        target_distance = abs(target[0]) + abs(target[1])
        for i in ghosts:
            if abs(target[0] - i[0]) + abs(target[1] - i[1]) <= target_distance:
                print()