
num1 = int(input())
num2 = int(input())

# Extracts the last 2 bits.
num1_last_2bits = num1 & 3
num2_last_2bits = num2 & 3

# XOR the last 2 bits of the numbers to make it 0’s.
num1 ^= num1_last_2bits
num2 ^= num2_last_2bits

# OR the number with that extracted bits to set those bits in that number’s last two bits.
num1 |= num2_last_2bits
num2 |= num1_last_2bits

print(num1, num2)