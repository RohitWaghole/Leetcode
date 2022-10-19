class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        items = list(counts.items())
        items.sort(key=lambda item:(-item[1],item[0]))
        return [item[0] for item in items[0:k]]