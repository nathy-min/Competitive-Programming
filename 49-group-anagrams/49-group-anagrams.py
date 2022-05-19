class Solution(object):
    def groupAnagrams(self, strs):
        """
        """
        lookup=defaultdict(list)
        for s in strs:
            key="".join(sorted(list(s)))
            lookup[key].append(s)
        return [l for l in lookup.values()]    