class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        reverse_map = {}
        for k, v in enumerate(nums):
            if v in findNums:
                reverse_map[v] = k
        nums.reverse()
        stack = []
        result_list = []
        for i in nums:
            while True:
                if len(stack) == 0:
                    result_list.insert(0,-1)
                    stack.append(i)
                    break
                else:
                    if stack[-1] > i:
                        result_list.insert(0,stack[-1])
                        stack.append(i)
                        break
                    else:
                        stack.pop(-1)
        return list(map(lambda x: result_list[reverse_map[x]], findNums))