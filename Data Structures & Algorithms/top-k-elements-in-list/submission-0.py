class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        d = {k:nums.count(k) for k in nums}

        rank = sorted(list(d.values()))[::-1]
        k_rank = rank[:k]

        k_tops = []

        for k, v in d.items():
            if v in k_rank:
                k_tops.append(k)

        return k_tops




            