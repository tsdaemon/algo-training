from typing import List


def reduce(arr: List):
    if len(arr) >= 3 and arr[-3:] == [1, 0, 0]:
        # reduce terminal node to a null pointer
        arr[-3:] = [0]
        # try reducing further
        reduce(arr)
        

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        result = []
        val = -1

        def process_coma():
            result.append(val)
            if val == 0:
                # try performing reduction after empty nodes
                reduce(result)

        for i in range(len(preorder)):
            if preorder[i] == ",":
                process_coma()
            elif preorder[i] == "#":
                val = 0
            else:
                val = 1
        
        # one more time for the last value
        process_coma()

        return result == [0]