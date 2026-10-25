def valid_palindrome(s: str) -> bool:
    def is_palindrome_range(i: int, j: int) -> bool:
        """Helper function to check if a substring is a palindrome."""
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Mismatch found: try skipping either the left or the right character
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            
    return True