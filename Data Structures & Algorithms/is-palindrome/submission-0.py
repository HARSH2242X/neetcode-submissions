class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1 
        while(left < right):
            leftchar = s[left]
            rightchar = s[right]
            if not leftchar.isalnum():
                left += 1
            elif not rightchar.isalnum():
                right -= 1
            elif leftchar.lower() == rightchar.lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True