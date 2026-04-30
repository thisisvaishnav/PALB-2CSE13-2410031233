from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())


# Given Examples
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
