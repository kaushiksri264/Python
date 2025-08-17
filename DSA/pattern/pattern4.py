class Solution:
    #Function will print pattern2
    def pattern4(self,n):
        for i in range(1,n + 1): #Outer loop will run rows
            for j in range(1,i + 1):#inner loop will run for columns
                print(i, end="")
            """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern4(n)

if __name__ == "__main__":
    Solution().main()
