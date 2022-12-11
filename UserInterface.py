import YoutubeDownloader
import tkinter as tk
class App(tk.Tk):
    def __init__ (self):
        super().__init__()

        self.title("Youtube Downloader")

        self.geometry('400x200')

        self.resizable(False, False)

        self.link = tk.Entry(master=self, width=30)

        self.link.pack(padx=5, pady=5, side=tk.TOP, fill=tk.X)
        
        self.download = tk.Button(master=self, text="Descargar", command = lambda: self.descargar())
        
        self.download.pack(padx=5, pady=5, side=tk.TOP, fill=tk.X)



        self.lista = tk.Listbox()



        self.lista.pack(padx=5, pady=5, side=tk.BOTTOM, fill=tk.X)



        self.mainloop()


    def descargar(self):
        yt = YoutubeDownloader.YDownloader('')

        yt.setPlaylist(self.link.get())
        
        yt.getPlaylist()
        for video in yt.getList():
            self.lista.insert(0, video)

        self.link.delete(0, tk.END)

        yt.convertSongs()


if __name__ =="__main__":
    app = App()
