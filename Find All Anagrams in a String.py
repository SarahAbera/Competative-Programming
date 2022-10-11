class Solution(object):
    def findAnagrams(self, s, p):
        anag = []
        map = Counter(p)
        dist= len(map)
        i,j = 0,0
        k = len(p)
        while(j < len(s)):
            if s[j] in map:
                map[s[j]] -= 1
                if(map[s[j]] == 0): dist -= 1
            if(j - i + 1 < k): j += 1
            else:
                if(dist == 0): anag.append(i)
                if s[i] in map: 
                    map[s[i]] += 1
                    if(map[s[i]] == 1): dist += 1
                i += 1
                j += 1
        return anag
