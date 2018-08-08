class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for _ops in ops:
            if _ops == "C":
                stack.pop(-1)
            elif _ops == "D":
                stack.append(2 * stack[-1])
            elif _ops == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(_ops))
        return sum(stack)
