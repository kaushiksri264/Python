class Solution:
    #Function will print pattern2
    def pattern17(self,n):
        for i in range(n):
            #Outer loop will run rows
            for j in range(n-i-1):
                print(" ", end ="")

            ch  = 'A'
            breakpoint = (2 * i + 1)//2
            for j in range(1, 2 * i + 2):#inner loop will run for columns
                print(ch, end="")
                if j<=breakpoint:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
                """ As soon as the n starts are printed move to next line"""
            print()

    def main(self):
        n = 5
        sol = Solution()
        sol.pattern17(n)

if __name__ == "__main__":
    Solution().main()