class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change_dict = {5:0, 10:0}
        for _bills in bills:
            if _bills == 5:
                #add to change_dict
                change_dict[5] += 1
            else:
                if _bills == 10:
                    if change_dict[5] == 0:
                        return False
                    else:
                        change_dict[10] += 1
                        change_dict[5] -= 1
                if _bills == 20:
                    # change = 5 + 10
                    if change_dict[5] > 0 and change_dict[10] > 0:
                        change_dict[5] -= 1
                        change_dict[10] -= 1
                    # change = 5 * 3
                    elif change_dict[5] >= 3:
                        change_dict[5] -= 3
                    else:
                        return False
        return True

