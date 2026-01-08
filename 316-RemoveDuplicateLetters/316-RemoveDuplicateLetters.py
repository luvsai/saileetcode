# Last updated: 08/01/2026, 19:56:17
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #we maintain a stack will preserve the order of smalles lexicographical words and doesnt contain duplicates.
        # data structures we need would be stack and visited set character.
        #algo
        # if top of stack is greater than the iterator cahracter and last index of the top element is greater than current iterator index than we replace it. end return the stack join in
        stack = []
        visited = set()
        last_char_index = {}
        # we need last occurence position of each character in the string
        for idx, ch in enumerate(s):
            last_char_index[ch] = idx

        for idx, ch in enumerate(s):
            if not stack:
                stack.append(ch)
                visited.add(ch)
                continue
            if ch in visited:
                continue
            while stack and stack[-1] > ch and last_char_index[stack[-1]] > idx:
                top = stack.pop()
                visited.discard(top)
            stack.append(ch)
            visited.add(ch)

        return "".join(stack)

