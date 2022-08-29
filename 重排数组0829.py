class Solution:
    def shuffle(self, nums):
        n = int(len(nums)/2)
        index = [0]*(2*n)
        nn = range(2*n)
        for i in nn:
            if i < n:
                index[2*i] = nums[i]
            else:
                index[(i-n)*2+1] = nums[i]
        self.result = index
        return self.result

if __name__ == '__main__':
    a = Solution()
    sss = [1,2,3,4,5,6,7,8,9,10]
    b = a.shuffle(sss)
    print(b)