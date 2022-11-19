class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        Up = self.run_chain(trees)
        Down = self.run_chain(trees[::-1])
        return set(Up + Down)

    def run_chain(self, stree):
        fence = []
        for p in stree:
            while len(fence)>=2 and self.check(fence[-2],fence[-1],p)>0:
                    fence.pop()
            fence.append(tuple(p))
        return tuple(fence)

    def check(self, h0, h1, h2):
        return  (h1[0] - h0[0])*(h2[1] - h1[1]) - (h1[1] - h0[1])*(h2[0] - h1[0])
