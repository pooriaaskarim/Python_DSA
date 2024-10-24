# Unadorned integer literals (whole numbers)
x = 10  # Positive integer
y = -5  # Negative integer
z = 0  # Zero is also an integer

# Operations with integers
sum_result = x + y  # Addition (10 + -5 = 5)
sub_result = x - y  # Subtraction (10 - -5 = 15)
mul_result = x * y  # Multiplication (10 * -5 = -50)
div_result = x // y  # Integer division (10 // -5 = -2)
mod_result = x % y  # Modulo (remainder) (10 % -5 = 0)

print(f"Sum: {sum_result}, Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}, Integer Division: {div_result}, Modulo: {mod_result}")

# more complex representation of integers in Python ( Unadorned Integer Literals )

# ## Different Bases
# Decimal (Base 10)

decimal_int1 = 123456  # Positive decimal integer
decimal_int2 = 0  # Zero as an integer
decimal_int3 = -98765  # Negative decimal integer

# Binary (Base 2)

binary_int1 = 0b1010  # Binary for decimal 10
binary_int2 = 0B1111  # Binary for decimal 15 (upper-case B also works)
binary_int3 = -0b1001  # Negative binary for decimal -9

# Octal (Base 8)

octal_int1 = 0o12  # Octal for decimal 10
octal_int2 = 0O17  # Octal for decimal 15 (upper-case O also works)
octal_int3 = -0o21  # Negative octal for decimal -17

# Hexadecimal (Base 16)

hex_int1 = 0xA  # Hexadecimal for decimal 10
hex_int2 = 0Xf  # Hexadecimal for decimal 15 (lower-case and upper-case letters work)
hex_int3 = 0x1F  # Hexadecimal for decimal 31
hex_int4 = -0X10  # Negative hexadecimal for decimal -16

# ## Different Representations

large_decimal = 1_000_000          # Decimal with underscores
large_binary = 0b1010_0001         # Binary with underscores
large_octal = 0o1_234_567          # Octal with underscores
large_hex = 0x1F_A3_B2             # Hexadecimal with underscores