#User function Template for python3

class Solution: 
    
    def select(self, arr, i):
        # code here 
        min_ind = i
        for ind in range(i, len(arr)):
            if(arr[ind] < arr[min_ind]):
                min_ind = ind
        return min_ind
        
    
    def selectionSort(self, arr,n):
        for ind in range(len(arr)):
            min_ind = self.select(arr, ind)
            arr[ind], arr[min_ind] = arr[min_ind], arr[ind]

            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())    #number of test cases
    for _ in range(t):  
        n = int(input())    # the size of the current test array
        arr = list(map(int, input().strip().split()))   # the current test array, space separated
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends