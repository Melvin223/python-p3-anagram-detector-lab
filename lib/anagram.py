class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, candidates):
        matches = []
        for candidate in candidates:
            candidate = candidate.lower()
            if (
                self.sorted_word == ''.join(sorted(candidate)) and
                self.word != candidate
            ):
                matches.append(candidate)
        return matches