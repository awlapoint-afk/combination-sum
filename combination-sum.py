class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates_len = len(candidates)

        def find_combo(combo, remaining, index):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return

            for i in range(index, candidates_len):
                combo.append(candidates[i])
                find_combo(combo, remaining - candidates[i], i)
                combo.pop()

        find_combo([], target, 0)
        return result


solution = Solution()

print(solution.combinationSum([2,3,6,7], 7))