class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "[" not in s:
            return s
        else:
            result = ""
            index = 0
            while index < len(s):
                if s[index] in ["0","1","2","3","4","5","6","7","8","9"]:
                    repeat_start = index + s[index:].find("[")
                    repeat_end = 0
                    repeat_time = int(s[index:repeat_start])
                    #find repeat_end
                    stack = 0
                    start_with_left = s[repeat_start:]
                    for i, value in enumerate(start_with_left):
                        if value == "[":
                            stack += 1
                        if value == "]":
                            stack -= 1
                        if stack == 0:
                            repeat_end =  i + repeat_start
                            break
                    for i in range(repeat_time):
                        result += self.decodeString(s[repeat_start + 1: repeat_end])
                    index = repeat_end + 1
                else:
                    result += s[index]
                    index += 1
            return result