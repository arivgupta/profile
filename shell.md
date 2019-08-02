# Morse Code Tutorial

In this tutorial, I will show you how to build a Morse Code Encryption Program using python.

## Pre Requisites
For this code, you will need to install...
[Py Charm Community](https://www.jetbrains.com/pycharm/download/#section=mac)
[Python 3](https://www.python.org/downloads/)

## Let's write some code...

First, you need to create a dictionary, which is denoted with squiggly brackets{}. A dictionary shows different keys and values, for which in our was, will be the letter corresponding to the morse code.

```
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
```

Next we need to define a function called encrypt that encrypts our English into Morse Code.
```
def encrypt(msg):
```

Then we need to define a string called cipher, which will be what the function returns as the encrypted message.
```
cipher = ''
```

Then we will create a for loop, that iterates through every letter in msg so that the function can look for each letter individually in our dictionary.
```
for letter in msg:
```

Noe we have to make sure that the letter does not equal space, as there is no difference in a Morse Code space than an English space.
```
if letter != ' ':
```

So if our code is not a space and it is a letter or a number, we will add the Morse Code equivalent of it by searching it up in out dictionary and adding it to cipher.  
```
cipher += morse[letter] + ' '
```

Now in case the input is not a letter of number and it is a space, we create an else statement.
```
else:
```

If it is a space, then all we need to do is add a space to our string called cipher.
```
cipher += ' '
```

Now we will return out string cipher as the output of the equation.        
```
return cipher
```

Now how will we get the user's input on what they want to encrypt. We will create a variable that will store the input called cleartextmessage.
```
cleartextmessage = input('Please enter the message you would like to encrypt: ')
```

Now we will make another variable called secretmessage to store call the function encrypt and store the result.
```
secretmessage = encrypt(cleartextmessage.upper())
```

Now we will print the encrypted message.
```
print(secretmessage)
```

And there you have it, a fully functional morse code encryption device built by yourself!

If you would like to download this code, click [here](Morse Code/MorseCode.py).
