class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        res=[]
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for i in range(k):
            highest = max(map.values())
            for key,value in map.items():
                if value==highest:
                    res.append(key)
                    map[key] = 0
                    break
        return res