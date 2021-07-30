from math import inf
def solve(s, word1, word2):
    i = 0
    length = len(s)
    length1 = len(word1)
    length2 = len(word2)
    dist = inf
    temp = inf
    found1 = False
    found2 = False
    while i < length:
        j1 = 0
        j2 = 0
        fail1 = False
        fail2 = False
        while i < length and s[i] != ' ':
            if j1 == length1:
                fail1 = True
            if j2 == length2:
                fail2 = True
            if not fail1:
                if j1 < length1 and word1[j1] == s[i]:
                    j1 += 1
                else:
                    fail1 = True
            if not fail2:
                if j2 < length2 and word2[j2] == s[i]:
                    j2 += 1
                else:
                    fail2 = True
            i += 1
        temp += 1
        if not fail1 and not fail2:
            return -1
        elif not fail1:
            if found2:
                dist = min(dist, temp - 1)
            temp = 0
            found1 = True
        elif not fail2:
            if found1:
                dist = min(dist, temp - 1)
            temp = 0
            found2 = True
        i += 1
    return dist
        
print(solve("dog ha cat hello cat dog dog hello cat world", "world", "hello"))