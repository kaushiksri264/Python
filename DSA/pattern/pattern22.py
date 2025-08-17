class Solution:
    #Function will print pattern2
    def pattern22(self,n):
        for i in range(2 * n - 1):
            for j in range(2 * n - 1):
               top = i
               left = j
               right = (2 * n - 2) - j
               bottom = (2 * n - 2) - i
               print(n - min(min(top,bottom), min(left,right)), end = "")
            print()

            
    def main(self):
        n = 5
        sol = Solution()
        sol.pattern22(n)

if __name__ == "__main__":
    Solution().main()