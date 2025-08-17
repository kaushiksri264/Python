class Solution:
    #Function will print pattern2
    def pattern20(self,n):
        inspaces = 2 * n - 2
        for i in range(1, 2 * n):
            stars = i
            if i > n:
                stars = 2 * n - i
            print("*" * stars, end ="")
            print(" " * inspaces, end="")
            print("*" * stars, end = "")
            print()
            if i < n:
                inspaces -= 2
            else:
                inspaces +=2

            
    def main(self):
        n = 5
        sol = Solution()
        sol.pattern20(n)

if __name__ == "__main__":
    Solution().main()