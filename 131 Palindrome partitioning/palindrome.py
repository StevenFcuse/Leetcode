class Solution(object):
    #function to calculate if a string is a palindrome
    def isPalindrome(self,s):
        if len(s) == 3:
            return True
        len_s = len(s)
        stopPoint = int(len_s/2)
        for i in range(0,stopPoint):
            if (s[i] != s[-i-1]): # len(s) - 1 - i
                return False
        return True
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        len_s = len(s)
        valid = [ [-1]*len_s for i in range(len_s)]
        #2d array with palindromes starting from n and ending at m
        #for loop from the beginning to find all palindromes and store them
        #this uses DP to check if the innermost palindrome has already been calculated
        #from the above 2d array
        for i in range(len_s):
            for j in range(i+1,len_s):
                if (s[i] == s[j]):
                    if (j - i) == 1:
                        valid[i][j] = 1
                    elif (valid[i+1][j-1] == 1):
                        valid[i][j] = 1
                    elif (valid[i+1][j-1] == 0):
                        valid[i][j] = 0
                    else:
                        valid[i][j] = self.isPalindrome(s[i:j+1])
        partition = []
        partition.append(list(s)) # add the palindrome partition with just single letters
        memoise = [[]] * len_s
        currPartition = []
        #use bottom up Dp to get all palindrome partitions from the valid 2d array and store it in a 1d array
        #memoise[n] stores all possible palindrome partitions starting from n
        #to calculate memoise[n] see if there's any palindrome starting from n and ending between n and the length of the string s
        # if there is a palindrome then add all the memoise[j] where j is greater than the end of the palindrome
        for i in range(len_s-1,-1,-1):
            prev = list(s[0:i])
            for j in range(i,len_s):
                if (valid[i][j] == 1):
                    someList = [prev + [s[i:j+1]] + list(s[j+1:len_s])] # add it in base partition
                    if (s[j+1:len_s] == ""):
                        memList = [[s[i:j+1]]]
                    else:
                        memList = [[s[i:j+1]] + list(s[j+1:len_s])]
                    basic = prev + [s[i:j+1]]
                    for v in range(j+1,len_s):
                        if memoise[v]:
                            for m in memoise[v]:
                                if (s[j+1:v] == ""):
                                    someList.append(basic+m)
                                    memList.append([s[i:j+1]] + m)
                                else:
                                    someList.append(basic+list(s[j+1:v])+m)
                                    memList.append([s[i:j+1]]+list(s[j+1:v])+m)
                    memoise[i] = memoise[i] + memList
                    for g in someList:
                        partition.append(g)
        return partition
        #in retrospect this solution is more messier than using recursion
        # and doing a double for loop to find all palindromes
        #than recursively calculating the other palindromes
        # to find all partitions
        # the main thing to think about when approaching this problem
        # is to think about how to actually get all possible palindrome partitions
        # of the given string before solving it.
