'''
https://leetcode.com/problems/find-k-closest-elements/

Did it run on leetcode: Yes
Did you face any problem : Yes

Time Complexity : 0(logn+K)
Space Complexity: 0(K)


Algorithm:
- Since the elements are sorted, we apply a binary search to find the element or the nearest element to our target.
- Then we traverse left and right from the searched index to check which are nearest elements and it to our list.


'''

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def findNearestIndex(target,distances):
            low,high = 0,len(distances)
            while low<high:
                mid = (low+high)//2
                if distances[mid]==target:
                    return mid
                elif distances[mid]>target:
                    high = mid
                else:
                    low=mid+1
            oneLeft,oneRight = abs(target-distances[low-1]),abs(target-distances[low])
            return low-1 if oneLeft<=oneRight else low
        idx = -1
        if x<=arr[0]:
            idx=0
        elif x>=arr[-1]:
            idx=len(arr)-1
        else:
            idx = findNearestIndex(x,arr)
        
        
        count =1
        ans = [arr[idx]]
        i,j=idx-1,idx+1
        
        while(count<k):
            if i<0:
                ans.append(arr[j])
                j+=1
                count+=1
            elif j>len(arr)-1:
                ans.append(arr[i])
                i-=1
                count+=1
            elif abs(x-arr[i])<=abs(x-arr[j]):
                ans.append(arr[i])
                i-=1
                count+=1
            else:
                ans.append(arr[j])
                j+=1
                count+=1
        ans.sort()
        return ans