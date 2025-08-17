class Solution:
    #Function will print pattern2
    def pattern18(self,n):
        for i in range(n): #Outer loop will run rows

            for ch in range(ord('A') + n - i - 1, ord('A') + n):
                print(chr(ch), end = "")
            """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern18(n)

if __name__ == "__main__":
    Solution().main()