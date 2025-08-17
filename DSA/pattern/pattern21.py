class Solution:
    #Function will print pattern2
    def pattern21(self,n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end = "")
                else:
                    print(" ",end="")
            print()

            
    def main(self):
        n = 5
        sol = Solution()
        sol.pattern21(n)

if __name__ == "__main__":
    Solution().main()