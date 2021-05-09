class Solution:
    def isPalindrome(self, num: int) -> bool:
        s = str(num)
        return s == s[::-1]
    
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        count, MAX = 0, 100000
        
        for i in range(MAX):
            s = str(i)
            n = int(s + s[-2::-1]) ** 2
            if n > right:
                break
            if n >= left and self.isPalindrome(n):
                count += 1
                
        for i in range(MAX):
            s = str(i)
            n = int(s + s[::-1]) ** 2
            if n > right:
                break
            if n >= left and self.isPalindrome(n):
                count += 1
        
        return count