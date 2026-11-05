class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words_hash = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in words_hash:
                words_hash[sorted_word] = [word]
            else:
                words_hash[sorted_word].append(word)
        
        return list(words_hash.values())
                
        