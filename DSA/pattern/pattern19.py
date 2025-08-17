class Solution:
    #Function will print pattern2
    def pattern19(self,n):
        spaces = 0
        for i in range(n): #Outer loop will run rows
            print("*" * (n - i),end = "")
            print(" " * spaces,end = "")
            print("*" * (n - i))
            spaces +=2
        inspaces = 2 * n - 2
        for i in range(1,n+1):
            print("*" * i, end ="")
            print(" " * inspaces, end="")
            print("*" * i)
            inspaces -=2
    def main(self):
        n = 5
        sol = Solution()
        sol.pattern19(n)

if __name__ == "__main__":
    Solution().main()