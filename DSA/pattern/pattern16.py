class Solution:
    #Function will print pattern2
    def pattern16(self,n):
        for i in range(n):
            #Outer loop will run rows
            ch  = chr(ord('A') + i)
            for j in range(i + 1):#inner loop will run for columns
                print(ch, end="")
                """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern16(n)

if __name__ == "__main__":
    Solution().main()