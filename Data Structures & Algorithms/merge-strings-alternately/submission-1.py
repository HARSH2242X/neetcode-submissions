class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = []
        left = 0 
        minlength = min(len(word1), len(word2))
        while(left<minlength):
            string.append(word1[left])
            string.append(word2[left])
            left +=1

        string.append(word1[left:])
        string.append(word2[left:])
        
        return "".join(string)

        
        
 