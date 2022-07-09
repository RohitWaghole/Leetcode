class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """
            clearly it is a DP problem. dp[i] represents the maxScore if you are at that idx
            
                    dp[i] = nums[i] + max(dp[i-k], dp[i-k+1].............dp[i-1)
                there will be k combos to find the max of ^^^
                -so since all of those combos will add nums[i]
					basically we just need to find the DP with the maxScore out of the k DPs before it
				-so dp[i] will equal nums[i] + the DP with the maxScore out of the k DPs before it
				
				-take this first test case as an example. let's say we are on idx3, value of 4 in the nums array
				-how do we find the best score at idx3? we have to take the max of the k DPs before it, k in this case is 3,
				-so looking at the 3 DPs before idx3, we have the dp values of 10, 5, and 8, so we choose the max of those
					which is 10 to add to our currNum, so 10+4 = 14, which becomes our dp[3]
		
				nums = [10,-5,-2,4,0,3], k = 3
				dp   = [10,5,8,14,14,17]
                                                        
            -obviously we could have looped thru all the k previous DPs to figure out that 10 was the max out of 10, 5 and 8
			but that is extremely inefficient
            -so we need to use a SLIDING WINDOW MAXIMUM algorithm wih deque!!!
				-if you aren't familiar with this algorithm, let me quickly explain as best as I can in easy terms
                -a deque is techncally a doubly-linkedlist, but don't let that scare you
				-we can just treat it like a list/array that can pop off from the beginning/end in O(1), that is why we use it
				-in our scenario, our deque's first element will ALWAYS hold the maxScore of the k DPs before idx i
            -each deque element will be a tuple (score, idx)
			-the deque should be thought of as a UTILITY tool that will help us maintain the max of the k DPs before our curr idx,
				and the length of the deque will most times not even be the same length as the window of size k
				-it serves solely to help store the maxScore of the k DPs before it at the first element. the rest of the elements in the
				deque are somewhat like a next in line type of thing.
				-so in our earlier example when we were at idx3,
					our deque should have looked like this [(10,0),(8,2)], 
					and then we could easily see that 10 is our maxScore from the k previous DPs, and we would add
					10 to our currNum of 4 at idx3 to become 14. you may be wondering why that deque did not have the
					score of 5 included in it, but you will see later why the score of 5 gets removed from the deque
					when we insert the score of 8
			-so how do we actually MAINTAIN this deque and keep the property where our first element is always
				the largest of the k DPs before our curr idx?
				-when we insert into the deque, if the back/right side of the deque has elements smaller than the one we are about to insert,
					then we need to keep popping it off, that way the larger value always bubbles left towards the first element,
						this is where our expression      while d and d[-1][0] < dp[i]: d.pop()       comes from
						-take for example we just finished processing dp[3] which we found earlier to be 14,
							at this current moment our deque looks like this [(10,0),(8,2)]
						-so if we were to insert 14, we would first need to pop off the 8, then since 14 is also greater than 10, the 10 gets
							popped off. so now the new deque is just [(14,3)]
				-we also have to keep in mind the case when our deque's first element falls outside of the window of size k
					-since i do the dp logic/updating before the deque maintainence in each iteration of the loop,
						if we are at idx4 in the loop then we are basically pre-computing the max of the k DPs for idx5,
						and for idx5 we would only consider the DP idxs of 2, 3 and 4. so since we are still in the loop for idx4, and our k is 3,
						if the deques first element is from idx1 or lower, then we need to delete it
							which is where the i-k == d[0][1] expression comes from
            
            nums = [10,-5,-2,4,0,3], k = 3
            dp   = [10,5,8,14,14,17]
            
		   this is what the deque looks likeat the beginning of each loop iteration
           deque =  [(10,0)]        idx1
			        [(10,0),(5,1)]  idx2
					[(10,0),(8,2)]  idx3  #here the 8 was larger than 5 so it popped off the 5
					[(14,3)]        idx4  #here the 14 was larger than 8 and 10 so both of those were popped off
					[(14,3),(14,4)] idx5
		"""
		
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0],0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]
            
            while d and d[-1][0] < dp[i]:   # sliding window maximum variation
                d.pop()                     # sliding window maximum variation
            d.append((dp[i],i))             # sliding window maximum variation
            
            if i-k == d[0][1]:              # sliding window maximum variation
                d.popleft()                 # sliding window maximum variation
                
        return dp[-1]