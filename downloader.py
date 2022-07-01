from pytube import YouTube
from pytube import Playlist

        # video downloader function
def download_youtube_video(link, path):
    try:
        yt = YouTube(link)
        
            #Showing details
        print("Title: ",yt.title)
        print("Number of views: ",yt.views)
        print("Length of video: ",yt.length)
        print("Rating of video: ",yt.rating)
            #Getting the highest resolution possible
        ys = yt.streams.get_highest_resolution()

            #Starting download
        print("Downloading...")
        ys.download(path)
        print("Download completed!!")
    except:
        print("Connection error OR please enter VIDEO link")
        
        
        # playlist downloader function
def download_youtube_playlist(link, path):
    try:
        pl = Playlist(link)
                #showing Playlist details
        print(f'Downloading Platlist : {pl.title}')
        PLAYLISTPATH = path + str(pl.title)

                #looping to videos one by one
        for video in pl.videos:
                    #Showing details of individual video downloads
            print("Downloading...Title: ",video.title)
                    #staring download
            ys = video.streams.get_highest_resolution()
            ys.download(PLAYLISTPATH)
            print("Downloaded ->", video.title)

        print("Download completed!!")

    except:
        print("Connection error\nOR\nPaste correct PLAYLIST link")
    
    
