import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    # TODO figure out if changing this would work
    "outtmpl": "../../Downloads/music_downloads/%(title)s-%(id)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}
# example
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k&list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG'])

"""
    out versioned post-processing options
    def convert(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            # TODO figure out if changing this would work
            "outtmpl": "../../Users/Donovan/Downloads/music_downloads/{}.mp3".format(self.name),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
"""