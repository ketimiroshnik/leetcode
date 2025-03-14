#49. Group Anagrams

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = dict()
    for i in range(len(strs)):
        x = "".join(sorted(list(strs[i])))
        if x in d:
            d[x].append(i)
        else:
            d[x] = [i]
    ans = []
    for x in d:
        mas = []
        for index in d[x]:
            mas.append(strs[index])
        ans.append(mas)
    return ans


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
