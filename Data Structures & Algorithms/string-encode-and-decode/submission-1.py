class Solution:
    key = "$melvin"

    def encode(self, strs: List[str]) -> str:
        word_lengths = []
        encoded_string = ""

        for word in strs:
            word_lengths.append(str(len(word)))
            encoded_string += word
        
        return ",".join(word_lengths) + "#" + encoded_string

        

    def decode(self, s: str) -> List[str]:
        word_lengths = []

        for i, char in enumerate(s):            
            if char == ",":
                continue
            
            if char == "#":
                s = s[i+1:]
                break
        
            word_lengths.append(int(char))
        
        start, end = 0, 0

        decoded_string = []

        for length in word_lengths:
            end = start + length
            decoded_string.append(s[start:end])
            start = end
        
        return decoded_string


        
        