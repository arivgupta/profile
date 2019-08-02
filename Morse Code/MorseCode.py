# accept user input in clear test
# convert each character into morse code
# dot = .
# dash = ---
# space = ' '

morse = {'A': '.---',
         'B': '---...',
         'C': '---.---.',
         'D': '---..',
         'E': '.',
         'F': '..---.',
         'G': '------.',
         'H': '....',
         'I': '..',
         'J': '.---------',
         'K': '---.---',
         'L': '.---..',
         'M': '------',
         'N': '---.',
         'O': '---------',
         'P': '.------.',
         'Q': '------.---',
         'R': '.---.',
         'S': '...',
         'T': '---',
         'U': '..---',
         'V': '...---',
         'W': '.------',
         'X': '---..---',
         'Y': '---.------',
         'Z': '------..',
         1: '.------------',
         2: '..---------',
         3: '...------',
         4: '....---',
         5: '.....',
         6: '---....',
         7: '------...',
         8: '---------..',
         9: '------------.',
         0: '---------------'}


def encrypt(msg):
    cipher = ''
    for letter in msg:
        if letter != ' ':
            cipher += morse[letter] + ' '
        else:
            cipher += ' '
            # print("cipher in progress: ", cipher)
    return cipher


def decrypt(msg):
    msg += ' '

    decipher = ''
    citext = ''
    for letter in msg:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values(reverse encryption)
                dict_idx = list(morse.values()).index(citext)
                decipher += list(morse.keys())[dict_idx]
                citext = ''
                dict_idx = ''
    return decipher


cleartextmessage = input('Please enter the message you would like to encrypt: ')  # type:object
secretmessage = encrypt(cleartextmessage.upper())
print(secretmessage)
decryptedmessage = decrypt(secretmessage)
print(decryptedmessage.lower())
