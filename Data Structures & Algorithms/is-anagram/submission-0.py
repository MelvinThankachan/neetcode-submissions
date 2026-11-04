class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_visited = {}
        t_visited = {}

        for char in s:
            if char in s_visited:
                s_visited[char] += 1
            else:
                s_visited[char] = 1
        
        for char in t:
            if char not in s_visited:
                return False
            
            if char in t_visited:
                t_visited[char] += 1
            else:
                t_visited[char] = 1

        return s_visited == t_visited