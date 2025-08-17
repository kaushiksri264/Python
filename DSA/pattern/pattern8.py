class Solution:
    #Function will print pattern2
    def pattern8(self,n):
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
        sol.pattern8(n)

if __name__ == "__main__":
    Solution().main()