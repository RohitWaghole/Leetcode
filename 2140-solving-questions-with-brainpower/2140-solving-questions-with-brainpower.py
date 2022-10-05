# class Solution:
#     def mostPoints(self, questions: List[List[int]]) -> int:
#         def f(i):
#             if i>=len(questions):
#                 return 0
#             pick = questions[i][0] + f(i+questions[i][1]+1)
#             notpick = 0 + f(i+1)
#             return max(pick, notpick)
#         return f(0)

#####################################################################################################

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [-1]*len(questions)
        def f(i,dp):
            if i>=len(questions):
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick = questions[i][0] + f(i+questions[i][1]+1,dp)
            notpick = f(i+1,dp)
            dp[i] = max(pick, notpick)
            return dp[i]
        return f(0,dp)