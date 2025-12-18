# Last updated: 18/12/2025, 20:17:51
# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []  # Stores all the generated case-permutated strings
        current_permutation = []  # Builds a single string character by character
        n = len(s)

        # Define the backtracking helper function
        # index: The current character position we are considering in the input string s
        def backtrack(index: int):
            # Base Case: If we have processed all characters of the input string
            if index == n:
                # A complete string has been formed, add it to the result list
                result.append("".join(current_permutation))
                return

            char = s[index]

            # If the current character is a digit, it must remain unchanged
            if char.isdigit():
                current_permutation.append(char)
                backtrack(index + 1)
                current_permutation.pop() # Backtrack: remove the digit
            else:
                # If the current character is a letter, we have two choices:

                # Choice 1: Append its lowercase form
                current_permutation.append(char.lower())
                backtrack(index + 1)
                current_permutation.pop() # Backtrack: remove the lowercase letter

                # Choice 2: Append its uppercase form
                current_permutation.append(char.upper())
                backtrack(index + 1)
                current_permutation.pop() # Backtrack: remove the uppercase letter

        # Start the backtracking process from the first character (index 0)
        backtrack(0)
        return result