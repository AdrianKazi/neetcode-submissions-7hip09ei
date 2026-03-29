class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            rest_days = temperatures[i+1:]
            curr_day_map = [temperatures[i]] * len(rest_days)

            higher_temp_map = [1 if rest > curr else 0 for rest, curr in zip(rest_days,curr_day_map)]

            if 1 in higher_temp_map:
                higher_temp_idx = higher_temp_map.index(1) + 1
            else:
                higher_temp_idx = 0

            res.append(higher_temp_idx)

        return res
