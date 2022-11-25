class Solution:
    def isValid(self, s: str) -> bool:
        hs={')':'(', ']':'[', '}':'{'}
        arr=''
        for i in s:
            if i in hs:
                if not arr or arr[-1] != hs[i]:
                    return False
                arr = arr[: - 1]
                
            else:
                arr+=i
        length = len(arr)
        return length == 0
        