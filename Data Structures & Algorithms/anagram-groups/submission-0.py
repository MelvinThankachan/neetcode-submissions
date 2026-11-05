class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
                
                # if second_word in visited:
                #     continue
                
                # visited.add(second_word)

                if len(second_word) != word_len:
                    continue
                
                if set(second_word) == word_set:
                    anagrams.append(second_word)
                    visited.add(second_word)
                
                
            result.append(anagrams)
        
        return result
                
                
                
                


