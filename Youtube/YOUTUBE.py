import pafy


def video(url):
    mp4 = pafy.new('https://www.youtube.com/watch?v=' + url)
    best = mp4.getbest()
    best.download(quiet=False)
    print("Download Complete")


def audio(url):
    mp3 = pafy.new('https://www.youtube.com/watch?v=' + url)
    best = mp3.getbestaudio()
    best.download(quiet=False)
    print("Download Complete")


ID = input('Insert the Video ID that you would like to download: ')

answer = input('Would you like to download the audio or video: ')

if answer == 'video':
    video(ID)
if answer == 'audio':
    audio(ID)
