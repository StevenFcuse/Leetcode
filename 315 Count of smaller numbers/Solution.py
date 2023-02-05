class Solution(object):

    def recursive(self, nums):
        num_length = len(nums)
        if (num_length == 1):
            return nums,[0],[0]
        mid = (num_length)//2
        leftArr,leftOutput,leftOrd = self.recursive(nums[0:mid])
        rightArr,rightOutput,rightOrd = self.recursive(nums[mid:num_length])
        left = 0
        right = 0
        ordList = []
        incCount = 0
        newList = []
        outputList = []
        while(True):
            if (left == len(leftArr) and right == len(rightArr)):
                break
            elif (left == len(leftArr)):
                newList.append(rightArr[right])
                outputList.append(rightOutput[right])
                ordList.append(rightOrd[right] + len(leftOrd))
                right += 1
                continue
            elif (right == len(rightArr)):
                newList.append(leftArr[left])
                leftOutput[left] += incCount
                outputList.append(leftOutput[left])
                ordList.append(leftOrd[left])
                left += 1
                continue
            if (leftArr[left] > rightArr[right]):
                newList.append(rightArr[right])
                outputList.append(rightOutput[right])
                ordList.append(rightOrd[right] + len(leftOrd))
                right += 1
                incCount += 1
                continue
            else:
                newList.append(leftArr[left])
                leftOutput[left] += incCount
                outputList.append(leftOutput[left])
                ordList.append(leftOrd[left])
                left += 1
        return newList,outputList,ordList


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # the solution used for this uses merge sort
        # A simple solution using two for loops would be O(n^2)
        # while a proposed merge sort solution is O(log(n))
        # The main thing to notice for this solution
        # is that given two sorted arrays calculating the count of smaller elements to the right
        # of each element is possible in O(n) time
        # this solution uses recursion when sorting the array it needs 3 outputs from the left and right subarrays
        # it needs the sorted array, the array with the running count of smaller elements to the right of each
        # element in the array and finally the position of each count in the original position
        testing,output,finalOutput = self.recursive(nums)
        finalOut = [-1] * len(nums)
        counter = 0
        for i in finalOutput:
            finalOut[i] = output[counter]
            counter += 1
        return finalOut
