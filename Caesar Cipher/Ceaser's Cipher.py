# create a program to encrypt using caesar ciphers
# make a loop to iterate through letters and then shift them by the specified amount

import enchant

d = enchant.Dict("en_US")

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(msg, key):
    counter = 0
    num = 0
    ciphertext = ''
    while counter < len(msg):
        symbol = msg[counter]
        if symbol in letters:
            num = letters.find(symbol)
            num = num + key
            if num >= len(letters):
                num = num - len(letters)
            ciphertext = ciphertext + letters[num]
        else:
            ciphertext = ciphertext + symbol
        counter += 1
    return ciphertext


def decrypt(msg):
    possible_solutions = []
    for i in range(26):
        deciphertext = ''
        for symbol in msg:
            num = letters.find(symbol) + i
            if num >= len(letters):
                num = num - len(letters)
            deciphertext += letters[num]
            if symbol != letters:
                deciphertext += symbol
        if d.check(deciphertext):
            possible_solutions.append(deciphertext)
    return possible_solutions


text = input("Enter message to be encrypted: ")
shift = input("Enter shift: ")

cipher = encrypt(text.upper(), int(shift))
print(cipher)
decipher = decrypt(cipher)
print('Possible answers for this encryption are: ', decipher)
