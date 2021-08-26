from typing import List


def reduce(arr: List):
    if len(arr) >= 3 and arr[-3:] == [1, 0, 0]:
        # reduce terminal node to a null pointer
        arr[-3:] = [0]
        # try reducing more
        reduce(arr)
        

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        result = []
        last_non_empty_node_idx = -1
        val = -1
        for i in range(len(preorder)):
            if preorder[i] == ",":
                result.append(val)
                if val == 0:
                    # try performing reduction
                    reduce(result)
            elif preorder[i] == "#":
                val = 0
            else:
                val = 1
        return result == [0]