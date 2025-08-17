class Solution:
    #Function will print pattern2
    def pattern6(self,n):
        for i in range(0,n): #Outer loop will run rows
            for j in range(n - i):#inner loop will run for columns
                print(j + 1, end=" ")
            """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern6(n)

if __name__ == "__main__":
    Solution().main()