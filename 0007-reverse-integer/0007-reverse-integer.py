class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_negative = x < 0  # Check if the number is negative
        x = abs(x)  # Work with the absolute value of x

        while x > 0:
            last_digit = x % 10
            x //= 10  # Use integer division to remove the last digit
            rev = rev * 10 + last_digit

        if is_negative:
            rev = -rev

        # Handle overflow cases (32-bit signed integer range)
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev

        
        