# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
#         if 0<=start<len(arr) and arr[start]>=0:
#             arr[start]=-arr[start]
#             return arr[start]==0 or self.canReach(arr, start+arr[start]) or self.canReach(arr,start-arr[start])
#         return False
    
##########################################################################################################

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = [start]
        while len(queue)>0:
            
            size = len(queue)
            
            for _ in range(size):
                point = queue.pop(0)
                
                # for left side i-arr[i]
                if (point-arr[point])>=0:
                    if arr[point - arr[point]]==0:
                        return True
                    elif arr[point - arr[point]]>0:
                        queue.append(point - arr[point])
                    
                # for right side i+arr[i]
                if (point+arr[point])<len(arr):
                    if arr[point + arr[point]]==0:
                        return True
                    elif arr[point + arr[point]]>0:
                        queue.append(point + arr[point])
                    
                arr[point] = -arr[point]
        return False
