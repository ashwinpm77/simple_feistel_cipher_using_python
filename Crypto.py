# Feistel Cipher (Modified)

import sys
import random



# XOR function
def xor(a, b):
    output = ""
    for _ in range(len(a)):
        if a[_] == b[_]:
            output += "0"
        else:
            output += "1"
    return output
# Complement function

# Key Generator Function
def key_generator(initkey, no_of_keys):
    keys = []
    key = initkey
    for _ in range(no_of_keys):
        key = (key+key[0])[1:]
        keys.append(key)
    return keys

def cipher(inp, keys, f):
    output = []
    for i in inp:
        intr = i
        Ln = ""
        R = ""
        for key in keys:
            L, R = intr[:32], intr[32:]
            Ln = xor(L, f(key, R))
            intr = R+Ln
        output.append(Ln+R)
    return output
    


# Function to convert text to binary array
def text_to_binarray(text):
    bin_array = []
    text_bin = ""
    for i in text:
        x = bin(ord(i))[2:]
        if len(x) < 8:
            text_bin += (("0"*(8-len(x))) + x)
        else:
            text_bin += x
    ptlen = len(text_bin)
    if ptlen%64 != 0:
        x = ptlen%64
        text_bin += ("0"*(64-x))
    ptlen = len(text_bin)
    for i in range(0, ptlen, 64):
        bin_array.append(text_bin[i:i+64])
    return bin_array


# Function to convert binary array to text
def bin_array_to_text(bin_array):
    text = ""
    for _ in bin_array:
        for __ in range(0, 64, 8):
            text += chr(int(_[__:__+8], 2))
    return text



            
    



# def something(consts):
#     y = []
#     for i in consts:
#         x = bin(int(i, 16))[2:]
#         xl = len(x)
#         if xl < 32:
#             x = ("0"*(32-xl))+x
#         y.append(x)
#     return y
# len(something(s_box))


def main():
    if len(sys.argv) != 4:
        print("Enter proper commandline argument as\n<key_file> <e | d> <filename>\ne for encryption\nd for decryption\n<key_file> contains key (8 two digit hexadecimal seperated by space)\n<filename> contains the data")
    else:
        key = open(sys.argv[1], "r").read().split()[:8]
        option = sys.argv[2]
        file_data = open(sys.argv[3], "r").read()
        keys = key_generator("01101011000101100101110001010110", 16)
        if option == 'e':
            cipher_text = bin_array_to_text(cipher(text_to_binarray(file_data), keys, xor))
            open("crypto_output", "w").write(cipher_text)
        elif option == 'd':
            keys.reverse()
            plain_text = bin_array_to_text(cipher(text_to_binarray(file_data), keys, xor))
            open("crypto_output", "w").write(plain_text)
        else:
            print("Invalid option")

if __name__ == "__main__":
    # try:
        main()
    # except Exception:
        print("Error: check filenames exist or not.")
