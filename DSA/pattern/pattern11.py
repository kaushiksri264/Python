class Solution:
    #Function will print pattern2
    def pattern11(self,n):
         
         for i in range(0,n): #Outer loop will run rows
            start = 0
            if i % 2 == 0:
                start =1
            else:
                start = 0
            for j in range(0,i+1):#inner loop will run for columns
                print(start, end="")
                start = 1 - start
                """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern11(n)

if __name__ == "__main__":
    Solution().main()