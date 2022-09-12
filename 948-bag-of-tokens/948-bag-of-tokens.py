class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        queue = collections.deque(tokens)
        ans = bns = 0
        while queue and (power>=queue[0] or bns):
            while queue and power>=queue[0]:
                power -= queue.popleft()
                bns += 1
            ans = max(ans, bns)
            if queue and bns:
                power += queue.pop()
                bns -= 1
        return ans