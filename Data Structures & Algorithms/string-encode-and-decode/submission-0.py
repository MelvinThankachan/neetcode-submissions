class Solution:
    key = "$melvin"

    def encode(self, strs: List[str]) -> str:
        encoded_string = self.key.join(strs)
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        decoded_string = s.split(self.key)
        return decoded_string