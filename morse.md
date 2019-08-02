# Morse Code Tutorial

In this tutorial, I will show you how to build a Morse Code Encryption and Decryption Program using python.

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

Now we will make another variable called secretmessage to store call the function encrypt and store the result. We have upper() here to turn our words into uppercase as our dictionary only includes uppercase letters.
```
secretmessage = encrypt(cleartextmessage.upper())
```

Now we will print the encrypted message.
```
print(secretmessage)
```

Now let's make another function called decrypt so that we can decrypt out message.
```
def decrypt(msg):
```
Lest give our coded message msg a space so that we can check where a new word appears.
    ```
    msg += ' '
    ```
Let's create a string decipher to be the decoded message that we will be decoding.
    ```
    decipher = ''
    ```
Let's create another string called citext. The reason we are making this is so that when we iterate through morse code, since it is not one letter, we will need to add dots and dashes to this string until the for loop that we are about to initiate senses a space.
    ```
    citext = ''
    ```
Now we will iterate through every 'letter' in our morse code so that we can find the index, or placement of that value in our dictionary.
    ```
    for letter in msg:
    ```
How again, we have to say that if the letter does not equal a space, a part of the omrse code will be added to the string citext.
    ```
        if letter != ' ':
    ```
Then the counter i will equal zero.
    ```
          i = 0
    ```
Then add the morse dash--- or dot to the string citext.
    ```
          citext += letter
    ```
Otherwise
    ```
          else:
    ```
The counter i would equal 1 if the function senses a space as that would separate each letter of the morse code.
    ```
            i += 1
    ```
Otherwise, if i equals 2, which it only would if the word ended and a new word begun, as remember on the beginning of this, we added a space to our message to show the end of the word, and here is where we are using it.
    ```
            if i == 2:
    ```
Add a space to decipher as the word ended.
          ```
            decipher += ' '
          ```
Otherwise, this would be if i = 0...
            ```
            else:
            ```
Make a new variable called dict_idx to store the index, or where the value of the morse code is stored in the dictionary.
                ```
    dict_idx =list(morse.values()).index(citext)
                ```
This is adding the letter in morse code to our string decipher but finding the key in our dictionary which is the letter by using the index that we got previously.
                ```
      decipher += list(morse.keys())[dict_idx]
                ```
Now we are resetting our citext so that we can add those dots and dashes again.
                ```
                citext = ''
                ```
We are resetting our index variable so that we can find another inded for the next 'letter'
                ```
                dict_idx = ''
                ```
Now we return decipher as the output.
```    
return decipher
```
Let's make a variable that will call the decrypt function and save the answer.
```
decryptedmessage = decrypt(secretmessage)
```
Now we will print the decrypted message in lowercase assuming the user enters lowercase letters originally.
```
print(decryptedmessage.lower())
```
And there you have it, a fully functional morse code encryption device built by yourself!

If you would like to download this code, click [here](Morse Code/MorseCode.py).
