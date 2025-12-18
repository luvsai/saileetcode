# Last updated: 18/12/2025, 20:17:29
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0  # Tracks the balance of '(' and ')'
        moves = 0  # Counts the number of insertions required

        for char in s:
            if char == '(':
                balance += 1  # Opening parenthesis, increment balance
            else:  # char == ')'
                balance -= 1  # Closing parenthesis, decrement balance

                # If balance becomes negative, we have an unmatched ')'
                if balance < 0:
                    moves += 1  # Need to insert an opening parenthesis
                    balance = 0  # Reset balance since we "fixed" the excess ')'

        # After the loop, any positive balance indicates unmatched '('
        return moves + balance