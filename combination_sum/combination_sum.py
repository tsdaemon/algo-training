from typing import List

class Solution:
    def findCombSumRec(self, candidates: List[int], target: int, last_idx: int, combinations: List[List[int]], combination_candidate: List[int]):
        if last_idx == -1:
            return
        if target == 0:
            combinations.append(combination_candidate)
            return
        
        cand_val = candidates[last_idx]
        if cand_val <= target:
            combination_candidate2 = combination_candidate + [cand_val]
            self.findCombSumRec(candidates, target-cand_val, last_idx, combinations, combination_candidate2)
        
        self.findCombSumRec(candidates, target, last_idx-1, combinations, combination_candidate)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination_candidate = []
        candidates.reverse()
        self.findCombSumRec(candidates, target, len(candidates)-1, combinations, combination_candidate)
        return combinations