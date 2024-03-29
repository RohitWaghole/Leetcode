# TIME LIMIT EXCEED

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def update(self, index: int, val: int) -> None:
#         self.nums[index] = val

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


########################################################################################

# TIME LIMIT EXCEED

# class NumArray(object):
#     def __init__(self, nums):
#         self.update = nums.__setitem__
#         self.sumRange = lambda i, j: sum(nums[i:j+1])

##########################################################################################

# TIME LIMIT EXCEED

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.pref = [0]
#         for i in nums:
#             self.pref.append(self.pref[-1]+i)
#         self.n = len(self.pref)

#     def update(self, index: int, val: int) -> None:
#         diff = val - self.nums[index]
#         self.nums[index] = val
        
#         for i in range(index+1,self.n):
#             self.pref[i] += diff

#     def sumRange(self, left: int, right: int) -> int:
#         return self.pref[right+1] - self.pref[left]
    
##################################################################################################

# ACCEPTED

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.seg_tree = [dict() for _ in range(4*self.n)]
        
#         def build(i, j, indx):
#             self.seg_tree[indx]['left'] = i
#             self.seg_tree[indx]['right'] = j
            
#             if i == j:
#                 self.seg_tree[indx]['val'] = nums[i]
#                 return
            
#             mid = (i+j)//2
            
#             build(i, mid, 2*indx)
#             build(mid+1, j, 2*indx+1)
            
#             self.seg_tree[indx]['val'] =  self.seg_tree[2*indx]['val'] +self.seg_tree[2*indx+1]['val']
        
#         build(0,self.n-1,1) # start the tree from index 1
        
        
                
#     def update(self, index: int, val: int) -> None:
        
#         def seg_update(index, val, indx):
#             i = self.seg_tree[indx]['left']
#             j = self.seg_tree[indx]['right']
            
#             if i==j and i==index:
#                 self.seg_tree[indx]['val'] = val
#                 return
            
#             mid = (i+j)//2
            
#             if index<=mid:
#                 seg_update(index,val,2*indx)
#                 self.seg_tree[indx]['val'] =  self.seg_tree[2*indx]['val'] +self.seg_tree[2*indx+1]['val']
#             else:
#                 seg_update(index,val,2*indx+1)
#                 self.seg_tree[indx]['val'] =  self.seg_tree[2*indx]['val'] +self.seg_tree[2*indx+1]['val']
        
#         seg_update(index, val, 1)
        

#     def sumRange(self, left: int, right: int) -> int:
        
#         def query(left, right, indx):
#             i = self.seg_tree[indx]['left']
#             j = self.seg_tree[indx]['right']
            
#             if i == left and j == right:
#                 return self.seg_tree[indx]['val']
            
#             mid = (i+j)//2
            
#             if i <= left and right <=mid:
#                 return query(left,right,2*indx)
#             if mid+1<=left and right <= j:
#                 return query(left,right,2*indx+1)
            
#             lval = query(left, mid, 2*indx)
#             rval = query(mid+1, right, 2*indx+1)
            
#             return lval + rval
        
#         return query(left, right, 1)

#################################################################################################

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index, val):
        self.sums += val-self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
    
        if right-left < len(self.nums)//2:
            return sum(self.nums[left:right+1])
        return self.sums - sum(self.nums[:left]) - sum(self.nums[right+1:])