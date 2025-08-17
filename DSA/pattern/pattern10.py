class Solution:
    #Function will print pattern2
    def pattern10(self,n):
        self.upperside_pyramid(n)
        self.lowerside_pyramid(n)

    def upperside_pyramid(self,n):
        for i in range(0,n): #Outer loop will run rows
            for j in range(0,i + 1):#inner loop will run for columns
                print("*", end="")
                """ As soon as the n starts are printed move to next line"""
            print()
    def lowerside_pyramid(self,n):
        for i in range(0,n): #Outer loop will run rows
            for j in range(0,n - i -1):#inner loop will run for columns
                print("*", end="")
                """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern10(n)

if __name__ == "__main__":
    Solution().main()