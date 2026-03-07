def isAnagram(str1, str2):
    map = dict()
    if len(str1) != len(str2):
        return False

    n = len(str1)
    for i in range(n):
        map[str1[i]] = map.get(str1[i], 0) + 1
        map[str2[i]] = map.get(str2[i], 0) - 1

    s = set(map.values())
    if len(s) > 1:
        return False
    
    val = s.pop()
    if val == 0:
        return True
    else:
        return False
    
str1 = input()
str2 = input()

print(isAnagram(str1=str1, str2=str2))