class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        ranks.sort()
        d = Counter(ranks)
        for key,val in d.items():
            if val>=3:
                return "Three of a Kind"
        for i in range(len(ranks)-1):
            if ranks[i]==ranks[i+1]:
                return "Pair"
        return "High Card"