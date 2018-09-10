# Installation Instructions
To install this program, open command prompt (windows) / terminal (mac) and type ```git clone "REPO"```

The program requires other libraries to operate, some might not be downloaded on your computer.
####Installing ffmpeg:
 * Download the ffmpeg 
    * **(Windows)** Download the zip/rar file from the [website](https://ffmpeg.zeranoe.com/builds/) and extract it to a 
    location of your choice.
    * Open **command prompt** with admin access and enter ``setx /M PATH "path\to\ffmpeg\bin;%PATH%"`` with the "path" set to your ffmpeg
    directory. (An alternative would be using the control panel to edit system environmental variables)   
    * **(Mac)** ``brew install ffmpeg`` (if you do not have brew, you'll have to install it)
   
####Toubleshooting the program:  
   * Directories are unique for every user, while the program is designed to work across different platforms, you might have
   to manually change the download directory yourself.
        * The download directory is located in ``link.py`` under ``def convert()``, change this line: ``../../Downloads/music_downloads/``
        to your current download directory.