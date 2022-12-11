import pytube
import os
import moviepy.editor as mp
from shutil import rmtree
class YDownloader():
    def __init__(self, download):
        self.URL = download
        self.titles = list()
            
    def setPlaylist(self, download):
        
        self.titles.clear()
        
        self.URL = download
    
    def setSong(self, download):
        self.URL = download
    
    def getPlaylist(self):
        lista =  pytube.Playlist(self.URL)

        for video in lista.videos:
            try:
                cancion = video.streams.filter(file_extension='mp4').first()
                cancion.download(output_path=r'C:\Users\52322\Desktop\Youtube-Downloader\Videos')
                self.titles.append(video.title)
            
            except Exception as e:
                self.titles.append(f'Error: {e}')
    
    def convertSongs(self):

        dir_list = os.listdir(r'C:\Users\52322\Desktop\Youtube-Downloader\Videos')
    
        for i in dir_list:
            name = fr"C:\Users\52322\Desktop\Youtube-Downloader\Videos\{i}"
            print(name)
        
            clip = mp.VideoFileClip(name)
            
            clip.audio.write_audiofile(fr"C:\Users\52322\Desktop\Youtube-Downloader\Songs\{i[:-4]}.mp3")

            clip.close()

        rmtree(r'C:\Users\52322\Desktop\Youtube-Downloader\Videos')
        
        os.mkdir(r'C:\Users\52322\Desktop\Youtube-Downloader\Videos')

    
    def getList(self):
        return self.titles

    def getSong(self):
        tittle = ''
        
        video = pytube.YouTube(self.URL)
        
        try:
            cancion = video.streams.get_audio_only()
            cancion.download()
            tittle += video.title

        except Exception as e:
            tittle += "Error: "
            tittle += e

        tittle += '\n'

        return tittle