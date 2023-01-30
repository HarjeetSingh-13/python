class Solution():
    def __init__(self):
        print('1. Palindrome')
        print('2. Swapcase')
    def palindrome(self,v):
        return self.v==self.v[::-1]
    def swapcase(self,v):
        return self.v.swapcase()



obj = Solution()
obj.c=int(input())
obj.v=input()
if obj.c==1:
    print(obj.palindrome(obj.v))
elif obj.c==2:
    print(obj.swapcase(obj.v))