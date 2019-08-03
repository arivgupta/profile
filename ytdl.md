# Youtube Downloader Tutorial

In this tutorial, I will show you how to build a youtube audio and video downloader using python.

## Pre Requisites
For this code, you will need to install...
[Py Charm Community](https://www.jetbrains.com/pycharm/download/#section=mac)
[Python 3](https://www.python.org/downloads/)
The Pafy Library(enter (pip3 install pafy) in your terminal, if it asks for a permissions problem, run (sudo pip3 install pafy)
The Youtube DL Library(enter (pip3 install youtube-dl) in your terminal, if it asks for a permissions problem, run (sudo pip3 install youtube-dl)

## Let's write some code...

We will have to import the library pafy that we just downloaded to use it in our code. Since pafy utilizes it to download the links so we do not have to import youtube-dl.
```
import pafy
```

We are now going to create a function video that will download the video link from the Image ID.
```
def video(ID):
```


```
mp4 = pafy.new('https://www.youtube.com/watch?v=' + ID)
```

```
best = mp4.getbest()
```


```
best.download(quiet=False)
```


```
print("Download Complete")
```


```
def audio(ID):
```


```
mp3 = pafy.new('https://ww w.youtube.com/watch?v=' + ID)
```


```
best = mp3.getbestaudio()
```


```
best.download(quiet=False)
```


```
print("Download Complete")
```


```
ID = input('Insert the Video ID that you would like to download: ')
```

```
answer = input('Would you like to download the audio or video: ')
```


```
if answer == 'video':
```


```
video(id)
```


```
if answer == 'audio':
```


```
audio(id)
```

And there you have it, a youtube video and audio downloader built by yourself!

If you would like to download this code, click [here](Youtube/YOUTUBE.py).
