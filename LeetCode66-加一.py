class Solution:
    def plusOne(self, digits):
        dig = int(''.join(str(i) for i in digits))+1
        return [int(i) for i in list(str(dig))]