"""
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.
"""
class Solution:
    def Closest_MinMax( self, array ):
        minimum,maximum=float("inf"),float("-inf")
        for element in array:
            if element>maximum:
                maximum=element
            if element<minimum:
                minimum=element
        LastMinIndex,LastMaxIndex,result=-1,-1,len(array)
        for i in range(len(array)):
            if array[i]==minimum:
                LastMinIndex=i
                if LastMaxIndex>=0:
                    result=min(result,i-LastMaxIndex+1)
            if array[i]==maximum:
                LastMaxIndex=i
                if LastMinIndex>=0:
                    result=min(result,i-LastMinIndex+1)
        return  result
if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(Solution().Closest_MinMax(array))