'''
Question not present on leet code
Q:INPUT The input to the function/method consisits of three arguments: maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft; forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping route and the second integer represents the amount of travel distance required bu this shipping route; returnRouteList, a list of pairs of integers where the first integer represents the unique identifer of a return shipping route and the second integer represents the amount of travel distance required by this shipping route.

OUTPUT Return a list of pairs of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.

Example 1: Input: maxTravelDist = 7000 forwardRouteList = [[1,2000],[2,4000],[3,6000]] returnRouteList = [[1,2000]]

Output: [[2,1]]

Explanation: There are only three combinations [1,1],[2,1],and [3,1], which have a total of 4000, 6000, and 8000 miles, respectively. Since 6000 is the largest use that does tnot exceed 7000, [2,1] is the optimal pair.

Example 2: Input: maxTravelDist = 10,000 forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]] returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

Output: [[2,4],[3,2]]


Time Complexity : 0(N*logM)
Algorithm:
- for every forward route we will find closest possible in backward route list using binary search.
- Then we check with our running sum that our sum is less than that our not, to be added into our list.

'''


def search(arr,target):
    low,high = 0,len(arr)
    while low<high:
        mid = (low+high)//2
        if arr[mid][1]==target:
            return mid
        elif arr[mid][1]>target:
            high = mid
        else:
            low = mid +1
    return high-1


def searchPairs(forward,backward,target):
    result = []
    currSum = 0
    if len(forward)>len(backward):
        forward,backward = backward,forward
    sum = 0
    for i in range(len(forward)):
        forwardId,dist = forward[i]
        idx = search(backward,target-dist)
        if idx!=-1:
            currSum = dist+backward[idx][1]
            if sum<=currSum:
                sum = currSum
                if sum<currSum:
                    result = []
                result.append((forwardId,backward[idx][0]))
    return result


if __name__=="__main__":
    forward = [(1,2000),(2,4000),(3,6000)]
    backward = [(1,2000),(2,4000)]
    target = 7000
    print(searchPairs(forward,backward,target))