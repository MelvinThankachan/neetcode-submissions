class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def _is_anagram(word1, word2, n):
            word1_hash = defaultdict(int)
            word2_hash = defaultdict(int)
            
            i = 0
            while i < n:
                word1_hash[word1[i]] += 1
                word2_hash[word2[i]] += 1
                i += 1
            
            return word1_hash == word2_hash



        result = []
        n = len(strs)
        visited = set()

        for i, word in enumerate(strs):
            anagrams = [word,]
            word_set = set(word)
            word_len = len(word)

            if word in visited:
                continue
            visited.add(word)

            j = i
            while j < n - 1:
                j += 1
                second_word = strs[j]

                if len(second_word) != word_len:
                    continue
                
                if word == second_word:
                    continue
                
                if set(second_word) != word_set:
                    continue
                
                if _is_anagram(word, second_word, word_len):
                    anagrams.append(second_word)
                    visited.add(second_word)
                
                
            result.append(anagrams)
        
        return result
                
                
                
                


