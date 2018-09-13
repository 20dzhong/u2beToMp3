import youtube_dl


class video:

    def __init__(self, link, name, d_plist):
        self.link = link
        self.name = name
        self.d_plist = d_plist
        if not self.d_plist: self.strip()

    def strip(self):
        tmp = ""
        for i in range(len(self.link)):
            if self.link[i] == "&":
                break
            tmp += self.link[i]
        self.link = tmp
        return

    def convert(self):
        ydl_opts = {
            "outtmpl": "../../Users/Donovan/Downloads/music_downloads/{}".format(self.name),
            'postprocessors': [
                {'key': 'FFmpegMetadata'},
                {'key': 'FFmpegExtractAudio',
                 'preferredcodec': 'mp3',
                 'preferredquality': '192'},
            ]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])
            return

# below is the terminal command
# youtube-dl https://www.youtube.com/watch?v=BKANqfvcspQ --add-metadata --embed-thumbnail --extract-audio --audio-format mp3