class Solution:
    #Function will print pattern1
    def pattern1(self,n):
        for i in range(n): #Outer loop will run rows
            for j in range(n):#inner loop will run for columns
                print("*", end=" ")
            """ As soon as the n starts are printed move to next line"""
            print()
    
    def pattern2(self,n):
        for i in range(n): #Outer loop will run rows
            for j in range(i + 1):#inner loop will run for columns
                print("*", end=" ")
            """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern2(n)

if __name__ == "__main__":
    Solution().main()


    

    