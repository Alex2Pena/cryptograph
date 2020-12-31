# Takes in plain number and applies a shift
def encrypt(plain, shift):
    # Will eventually be the encrypted plain number
    encrypted_string = ""
    # Loop throuth each character and...
    for char in plain:
        # Convert each character into an integer
        digit = int(char)
        # Apply the amount of shift to the number
        shifted_digit = digit + shift
        # For each loop add the shifted number too the encrypted string
        encrypted_string += str(shifted_digit)
        print(encrypted_string)
    return encrypted_string


# decrypt by running encrypt with a -shift
def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


assert encrypt("hello", 2)
assert decrypt("3456", 2)
print('PAASSES')
