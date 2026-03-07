def isIsomorphic(str1, str2):
    map1 = dict()
    map2 = dict()

    for i in range(len(str1)):
        if map1.get(str1[i], None) is None:
            map1[str1[i]] = i
        if map2.get(str2[i], None) is None:
            map2[str2[i]] = i

        if map2[str2[i]] != map1[str1[i]]:
            return False
        
    return True

str1 = input()
str2 = input()
print(isIsomorphic(str1, str2))

