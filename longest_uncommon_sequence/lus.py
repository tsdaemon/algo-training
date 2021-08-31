from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # corner case: no items
        if len(strs) == 0:
            return -1
        # corner case: one item
        if len(strs) == 1:
            return len(strs[0])
        
        # first sort strings by length
        strs = list(sorted(strs, key=lambda s: (len(s), s), reverse=True))

        # if any is longer than others than it is the answer
        if len(strs[0]) > len(strs[1]):
            return len(strs[0])

        # itertively go over items checking if they have duplicates
        i = 0
        while i < len(strs):
            # go over the next items checking if there are duplicates
            j = i + 1
            duplicates = False
            while j < len(strs):
                if strs[i] == strs[j]:
                    duplicates = True
                else:
                    break
                j += 1
            
            if duplicates:
                # nothing to look here: jump to the first no duplicate item
                i = j
                continue

            # if no duplicates, lets check if it can be a substring of any previous item
            substring_of_previous = False
            for j in range(i):
                if strs[i] in strs[j]:
                    # nothing to do in this case, all substrings of this string are common
                    substring_of_previous = True
                    break

            if substring_of_previous:
                i += 1
                continue
            
            return len(strs[i])
        
        return -1



