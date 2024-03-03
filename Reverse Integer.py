class Solution(object):
    def reverse(self, x):
        neg = x< 0
        reverse_num=str(abs(x))[::-1]
        rev = -(int(reverse_num)) if neg else (int(reverse_num))
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        else:
            return 0
