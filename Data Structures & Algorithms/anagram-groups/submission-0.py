class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through the list
        # for each string in the list, sort the string and then use 
        # that for the key 
        # value is the string itself
        # after doing this all, return the values only as a list

        strDict = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key in strDict:
                strDict[key].append(s)
            else:
                strDict[key] = [s]
        
        print(list(strDict.values()))
        return list(strDict.values())
        