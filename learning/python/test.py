class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        rp = 0
        currentMaxC = ""
        currentMaxCount = 0
        result = 0
        currentStrDict = {}
        if len(set(s)) == len(s):
            return min(k+1,len(s))
        
        while rp < len(s):
            if lp == rp and rp!=0:
                rp+=1
                continue
            c = s[rp]
            if c in currentStrDict:
                currentStrDict[c] += 1
            else :
                currentStrDict[c] = 1
            
            if currentStrDict[c] > currentMaxCount:
                currentMaxC = c
                currentMaxCount = currentStrDict[c]
            
            currentElse = 0

            for i,v in currentStrDict.items():
                if i==c:
                    continue
                else:
                    currentElse+=v
            
            clp = s[lp]
            if currentElse>k:
                lp+=1
                currentStrDict[clp]-=1
                currentMaxC = max(currentStrDict,key = currentStrDict.get)
                currentMaxCount = currentStrDict[currentMaxC]

            result = max(result, rp-lp+1)
            rp+=1
        return result


s = Solution()

print(s.characterReplacement("BAAAB",2))