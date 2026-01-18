class Anagram:
    """An anagram detector class that finds anagrams for a given word."""
    
    def __init__(self, word):
       
        self.word = word
        self.signature = sorted(word.lower())
    
    def match(self, list_of_candidates):
       
        results = []
        for candidate in list_of_candidates:
            # Skip if it's the same word (case-insensitive comparison)
            if candidate.lower() == self.word.lower():
                continue
            # Check if candidate is an anagram by comparing signatures
            if sorted(candidate.lower()) == self.signature:
                results.append(candidate)
        return results

