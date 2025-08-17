class Solution:
    #Function will print pattern2
    def pattern9(self,n):
        self.inverted_pyramid(n)
        self.erect_pyramid(n)

    def inverted_pyramid(self,n):
        for i in range(0,n):
            for k in range(0,(n-i -1)):
                print(" ", end="") #Outer loop will run rows
            for j in range(0,(i*2+1)):#inner loop will run for columns
                print("*", end="")
                """ As soon as the n starts are printed move to next line"""
            print()

    def erect_pyramid(self,n):
        for i in range(0,n):
            for k in range(0,i):
                print(" ", end="") #Outer loop will run rows
            for j in range(0,2*n - (i*2+1)):#inner loop will run for columns
                print("*", end="")
                """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern9(n)

if __name__ == "__main__":
    Solution().main()