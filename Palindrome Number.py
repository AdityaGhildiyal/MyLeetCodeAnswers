class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        tag=x[::-1]
        #tag=int(tag)
        if(tag==x):
            return 1
        else:
            return 0
