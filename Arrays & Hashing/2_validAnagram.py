class Solution:
    # Explanation:
    # First, check if s and t have the same length. If not, they cannot possibly be anagrams, so return 'False'.
    # If they do, create an empty dictionary for each string.abs
    # Then, loop through each character in both of the strings. If the characters we encounter are not
    # already keys in their respective dictionaries, we'll initialize them with a 'value' of 1.
    # This 'value' represents the count, e.g. how many occurences of that letter exist in the string so
    # far. If we've already seen it, we'll increment the count by 1.
    # At the end, check if the two dictionaries are equal. If yes, they are anagrams, return 'True'.
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}
        for (charS, charT) in zip(s, t):
            if charS not in mapS.keys():
                mapS[charS] = 1
            else:
                mapS[charS] += 1
            if charT not in mapT.keys():
                mapT[charT] = 1
            else:
                mapT[charT] += 1
        return mapS == mapT
            
