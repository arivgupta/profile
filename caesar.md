# Caesar Cipher Tutorial

In this tutorial, I will show you how to build a caesar cipher encryption and decryption program using python. At the moment, this only decrypts one word encryptions, but I encourage you to create a remix to this and decrypt whole sentences. If you do not know what a caesar's cipher is, it is a cipher that shifts every letter that the sender writes a custom amount. So if I want to send my friend something like hi, and I want to shift it by 3, it will become KL.

## Pre Requisites
For this code, you will need to install...
- [Py Charm Community](https://www.jetbrains.com/pycharm/download/#section=mac)
- [Python 3](https://www.python.org/downloads/)
- The Pyenchant Library(enter (pip3 install pyenchant) in your terminal, if it asks for a permissions problem, run (sudo pip3 install pyenchant)

## Let's write some code...

We will have to import the library pyenchant so that when we decrypt our ciphers, we will be able to check them against a dictionary when we brute force the decryption.
```
import enchant
```

Now we will import this as an english dictionary. we will use this with the enchant.Dict() function.
```
d = enchant.Dict("en_US")
```

We will create a string with all of the letters of the alphabet so that we can use that to shift the letters the user inputs in the alphabet.
```
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

Now we will create a function called encrypt that will encrypt the words that the user inputs.
```
def encrypt(msg, shift):
```

We will create a counter that we will use to iterate through the letters that are in the word that the user inputs.
```
counter = 0
```

We will create another variable that will help us create a shift in the letters.
```
num = 0
```

We will create a variable to store the encrypted message.
```
ciphertext = ''
```

Now we will initialize a while loop to iterate through the letters in the word.
```
while counter < len(msg):
```

Let's create a variable called symbol that we will use as the iterated letter in the message.
```
symbol = msg[counter]
```

We will make an if statement to check if the symbol is in our letters.
```
if symbol in letters:
```

Then our num variable will equal the symbol index in our string letters.
```
num = letters.find(symbol)
```

Now we will add the shift that the user inputs to the index of the letter.
```
num = num + shift
```

Now we will make an if statement saying that if the number gets bigger than the length of the letters, as if you have a z in the word and you have a shift of 5, how will the index 25 reset to 1.
```
if num >= len(letters):
```

If this is true, then the number will equal itself minus the length of our letters string.
```
num = num - len(letters)
```

And then we will add the shifted letter to ciphertext by finding the letter using the index.
```
ciphertext += letters[num]
```

Now we will make an else statement in case someone writes a % sign that can not be shifted.
```
else:
```

Then we will just add it to our completed cipher.
```
ciphertext = ciphertext + symbol
```

At the ent, we will add one to the counter so that we can iterate through the message.
```
counter += 1
```

And now we will return ciphertext as the encrypted message.
```
return ciphertext
```

Now we will create a function called decrypt.
```
def decrypt(msg):
```

We will make a list called possible_solutions.
```
possible_solutions = []
```

Now we will, since we have to decrypt this message by checking through every possible shift, create a for loop that loops through 26 times with i as the counter.
```
for i in range(26):
```

Now we will create a variable to store the deciphered text.
```
deciphertext = ''
```

Now we will iterate through the encrypted message with a for loop.
```
for symbol in msg:
```

A new variable called num will equal the index of the letter in our letters string and add the shift of i to it.
```
num = letters.find(symbol) + i
```

Now we will make an if statement saying that if the number gets bigger than the length of the letters, as if you have a z in the word and you have a shift of 5, how will the index 25 reset to 1.
```
if num >= len(letters):
```

If this is true, then the number will equal itself minus the length of our letters string.
```
num = num - len(letters)
```

And then we will add the shifted letter to deciphertext by finding the letter using the index.
```
deciphertext += letters[num]
```

Now we will utilize our imported dictionary to check each word that is added on to deciphertext.
```
if d.check(deciphertext):
```
And if any of the words match a word in the dictionary, then we will add that word to the possible_solutions list using the append() funciton.
```
possible_solutions.append(deciphertext)
```

Now we will return possible_solutions as the answer.
```
return possible_solutions
```

We will create a variable called text to ask which message should be encrypted.
```
text = input("Enter message to be encrypted: ")
```

We will ask the user to enter the shift for the encryption.
```
shift = input("Enter shift: ")
```

Now we will make a new variable called cipher which called the encrypt function and inputs the two values of text as uppercase since we used uppercase in our string and the shift as an integer.
```
cipher = encrypt(text.upper(), int(shift))
```

Then we will print this cipher.
```
print(cipher)
```

Now we will decrypt the same cipher(you can create a new message to decrypt if you would like). This variable decipher will call the decrypt function and return the decrypted cipher.
```
decipher = decrypt(cipher)
```

Now we will print the possible answers for this encryption using our returned list from the function.
```
print('Possible answers for this encryption are: ', decipher)
```

And there you have it, a caesar cipher encryption and decryption program made by yourself!

If you would like to download this code, click [here](Caesar Cipher/Ceaser's Cipher.py).
