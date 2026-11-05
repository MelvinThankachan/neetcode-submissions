class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_hash = defaultdict(list)
        
        for word in strs:
            words_hash["".join(sorted(word))].append(word)
        
        return list(words_hash.values())