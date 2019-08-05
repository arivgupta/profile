# Youtube Downloader Tutorial

In this tutorial, I will show you how to build a youtube audio and video downloader using python.

## Pre Requisites
For this code, you will need to install...
- [Py Charm Community](https://www.jetbrains.com/pycharm/download/#section=mac)
- [Python 3](https://www.python.org/downloads/)
- The Pafy Library(enter (pip3 install pafy) in your terminal, if it asks for a permissions problem, run (sudo pip3 install pafy)
- The Youtube DL Library(enter (pip3 install youtube-dl) in your terminal, if it asks for a permissions problem, run (sudo pip3 install youtube-dl)

## Let's write some code...

We will have to import the library pafy that we just downloaded to use it in our code. Since pafy utilizes it to download the links so we do not have to import youtube-dl.
```
import pafy
```

We are now going to create a function video that will download the video link from the Image ID.
```
def video(ID):
```

Now we will create a variable called mp4 to store a new pafy file. As you can see, I have added the part of the youtube link that is consistent in every link there so that the user only has to put the ID of the video.
```
mp4 = pafy.new('https://www.youtube.com/watch?v=' + ID)
```

We will make another variable called bestvideo to get the best video quality from the link by calling the getbest() pafy function.
```
bestvideo = mp4.getbest()
```

Now calling the pafy download() function, we will download our bestvideo. Quiet=False hides a display of the download progress of the video. If you would like to see download progress, you can change that to quiet=True.
```
bestvideo.download(quiet=False)
```

Here, instead of video progress, when the download is finished, we can have the system print Download Complete.
```
print("Download Complete")
```

We are now going to create a function audio that will download the audio from the Image ID.
```
def audio(ID):
```

Now, just like the function before, we will make a new variable called mp3 to save the url with the ID that we input.
```
mp3 = pafy.new('https://www.youtube.com/watch?v=' + ID)
```

We will make another variable called bestaudio to get the best video quality from the link by calling the getbestaudio() pafy function.
```
bestaudio = mp3.getbestaudio()
```

Again, calling the pafy download() function, we will download our bestaudio. Quiet=False hides a display of the download progress of the video. If you would like to see download progress, you can change that to quiet=True.
```
bestaudio.download(quiet=False)
```

Here, instead of audio progress, when the download is finished, we can have the system print Download Complete.
```
print("Download Complete")
```

Now we will make a prompt that will take the user input of the ID that they would like to download and store that into the variable ID.
```
ID = input('Insert the Video ID that you would like to download: ')
```

Let us create another variable called answer that will ask the user if they would like to download the audio or video content of the link.
```
answer = input('Would you like to download the audio or video: ')
```

We will initialize a statement that if the user types that they want to download the video file...
```
if answer == 'video':
```

Then we will call the function video to download the video using their specific video ID.
```
video(id)
```

We will initialize a statement that if the user types that they want to download the audio file...
```
if answer == 'audio':
```

Then we will call the function audio to download the video using their specific audio ID.
```
audio(id)
```

And there you have it, a youtube video and audio downloader built by yourself! If you are having second thoughts about using this, I can assure you that this is legal. Extracting audio or video from a youtube link is legal.

If you would like to download this code, click [here](Youtube/YOUTUBE.py).
