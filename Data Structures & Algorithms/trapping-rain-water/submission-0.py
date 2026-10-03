class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1
        i_max=height[i]
        j_max=height[j]
        w = 0
        while(i < j):
            if(i_max < j_max):
                i+=1
                i_max = max(i_max, height[i])
                w += i_max - height[i]
            else:
                j-=1
                j_max = max(j_max, height[j])
                w += j_max - height[j]
        return w

            

