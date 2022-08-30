class Solution:
   def pancakeSort(self, arr):
      # 将最大值翻转到最后一位(需提前判断最大值不是最后一位)
      def rev(list1):
         len_list = len(list1)
         max_data = max(list1)
         max_index = list1.index(max_data)
         m = max_index + 1
         n = len_list
         list1[0:(max_index + 1)] = list(reversed(list1[0:(max_index+1)]))
         list2 = list(reversed(list1)).copy()
         list3 = list2[:-1]
         return m, n, list3

      result = []
      new_list = arr
      a = len(arr)
      while a > 1:
         print(a)
         print(new_list)
         sum = 0
         ind = range(a-1)
         for i in ind:
            if new_list[i+1] < new_list[i]:
               sum += 1
         if sum > 0:
            max_index1 = new_list.index(max(new_list))
            if max_index1 != (a - 1):
               aaa, bbb, new_list = rev(new_list)
               result.append(aaa)
               result.append(bbb)
            else:
               new_list = new_list[0:-1]
         else:
            break
         a = len(new_list)

      return result

if __name__ == '__main__':
   aaa = Solution()
   s = [1, 4, 5, 7, 2, 3]
   b = aaa.pancakeSort(s)
   print(b)