import youtube_dl
import subprocess
from utils import *
from link import *
from tkinter import *


# Dummy exceptions
class Empty_Name(Exception):
    pass


class Empty_Link(Exception):
    pass


class logs_var():
    def __init__(self, original=""):
        self.original = original

    def concat(self, new):
        self.original += new + "\n"
        return self.original


# functions for output and callback
def get_logs():
    # TODO Set logs to concatenate over time from terminal
    # TODO use get_logs to get time and print out the time last
    pass



