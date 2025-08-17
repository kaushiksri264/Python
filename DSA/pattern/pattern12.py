class Solution:
    #Function will print pattern2
    def pattern12(self,n):
         spaces = 2*(n-1)
         for i in range(1,n + 1): #Outer loop will run rows
            for j in range(1,i + 1):#inner loop will run for columns
                print(j, end="")
            for k in range(1,spaces + 1):
                print(" ", end ="")
            for j in range(i,0,-1):
                print(j,end = "")
                """ As soon as the n starts are printed move to next line"""
            print()
            spaces = spaces - 2

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern12(n)

if __name__ == "__main__":
    Solution().main()