class Solution:
    key = "$melvin"

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        word_lengths, encoded_string = [], []

        for s in strs:
            word_lengths.append(len(s))
            
        for length in word_lengths:
            encoded_string.append(str(length))
            encoded_string.append(',')

        encoded_string.append('#')
        encoded_string.extend(strs)
        return ''.join(encoded_string)
        
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        word_lengths, decoded_string, i = [], [], 0

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            word_lengths.append(int(s[i:j]))
            i = j + 1
        
        i += 1

        for length in word_lengths:
            decoded_string.append(s[i:i + length])
            i += length
            
        return decoded_string


        
        