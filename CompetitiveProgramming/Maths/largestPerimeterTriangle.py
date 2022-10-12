class Solution:

    def merge(self,low,m,high,arr):

        p = low

        q = m+1

        temp = []

        while(p <=m and q<=high):

            if(arr[p] >= arr[q]):
                temp.append(arr[p])
                p+=1

            else:
                temp.append(arr[q])
                q+=1

        while(p<=m):

            temp.append(arr[p])
            p+=1

        while(q<=high):
            temp.append(arr[q])
            q+=1

        arr[low:high+1] = temp



    def mergeSort(self,low,high,arr):

        if(low < high):

            m = (low + high) // 2

            self.mergeSort(low,m,arr)

            self.mergeSort(m+1, high, arr)

            self.merge(low,m,high,arr)



    def largestPerimeter(self, nums: List[int]) -> int:

        self.mergeSort(0,len(nums)-1,nums)

        for i in range(0,len(nums)-2):

            if(nums[i] < nums [i+1] + nums[i+2]):
                return nums[i]+nums[i+1]+nums[i+2]

        return 0 


            


