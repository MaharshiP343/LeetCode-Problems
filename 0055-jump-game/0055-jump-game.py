class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0 
        l = len(nums)
        maxpass = 0
        j=0
        if l == 1:
            return True
        while (True):        
            if (j >= l-1):
                print("pass",nums[i],maxpass,pas , i ,l)

                return True

            pas = nums[i]
            if maxpass <= pas:
                maxpass = pas
                print("pas update")
            print(nums[i],maxpass,pas , i ,l)

            
        
            
        
            print(nums[i],maxpass,pas , i)
            if maxpass == 0 and i != l-1:
                return False
            elif maxpass>0:
                j+=1
                maxpass -= 1
            i+=1

            

        
