class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + (' ' * spaces)
        sep_count = len(words) - 1
        spaces_between_words = spaces // sep_count
        spaces_in_the_end = spaces % sep_count
        return (' ' * spaces_between_words).join(words) + (' ' * spaces_in_the_end)