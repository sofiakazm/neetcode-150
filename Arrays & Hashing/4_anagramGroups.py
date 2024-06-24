class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        temp = {}
        count = -1
        for st in strs:
            sortedStr = ''.join(sorted(st))
            res = temp.get(sortedStr)
            if res != None:
                anagrams[res].append(st)
            else:
                count += 1
                anagrams.append([st])
                temp[sortedStr] = count
        return anagrams