class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1 
        while(left<right):
            leftchar = s[left]
            rightchar = s[right]
            if(leftchar == rightchar):
                left += 1
                right -= 1
            elif(self.checkpalindrome(s,left+1,right) or self.checkpalindrome(s,left,right-1)):
                return True
            else:
                return False
            
        return True


    def checkpalindrome(self , s:str , left:int , right:int) -> bool:
        while left < right:
            leftchar = s[left]
            rightchar = s[right]
            if(leftchar == rightchar):
                left +=1
                right -=1
            else:
                return False
    
        return True
    