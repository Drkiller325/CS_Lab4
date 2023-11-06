import random
def hex_to_bin(hex_key):
    # Convert a hexadecimal key to a binary key
    bin_key = bin(int(hex_key, 16))[2:].zfill(64)
    return bin_key

def initial_key_permutation(bin_key):
    # Define the PC-1 permutation table
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    # Apply the PC-1 permutation to the 64-bit binary key
    permuted_key = ''.join(bin_key[bit - 1] for bit in pc1_table)

    return permuted_key

# Example usage
hex_key = ''.join(random.choice('0123456789ABCDEF') for _ in range(8))
bin_key = hex_to_bin(hex_key)
permuted_key = initial_key_permutation(bin_key)

print("Original Hex Key:", hex_key)
print("Binary Key:", bin_key)
print("Permuted Key (After PC-1):", permuted_key)
