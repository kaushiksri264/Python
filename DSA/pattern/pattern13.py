class Solution:
    #Function will print pattern2
    def pattern13(self,n):
        num = 1
        for i in range(1,n + 1):
            #Outer loop will run rows
            for j in range(1,i+1):#inner loop will run for columns
                print(num, end="")
                num += 1
                """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern13(n)

if __name__ == "__main__":
    Solution().main()