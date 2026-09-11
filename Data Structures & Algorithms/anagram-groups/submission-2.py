class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for i,s in enumerate(strs):
            map["".join(sorted(s))] = []
        for s in strs:
            sort = "".join(sorted(s))
            if sort in map:
                map[sort].append(s)
        return list(map.values())