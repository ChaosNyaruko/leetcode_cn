class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for str in strs:
            counter = [0] * 26
            for c in str:
                counter[ord(c) - ord('a')] += 1

            m[tuple(counter)].append(str)

        return list(m.values())
