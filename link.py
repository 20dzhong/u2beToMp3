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
            'format': 'bestaudio/best',
            # TODO figure out if changing this would work
            "outtmpl": "../../Downloads/music_downloads/{}.mp3".format(self.name),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])
            return

