def group_anagrams(strs):
    groups = {}
    for word in strs:
        key = ""
        letters = sorted(word)
        for ch in letters:
            key += ch
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    result = []
    for key in groups:
        result.append(groups[key])
    return result


strs = input("Enter strings separated by space: ").split()
print("Grouped anagrams:", group_anagrams(strs))
