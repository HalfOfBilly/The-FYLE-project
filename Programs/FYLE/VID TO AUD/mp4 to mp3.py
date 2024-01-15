import sys
import os

from moviepy.editor import *

arg = sys.argv
    
mp4_file = arg[1]

export = arg[2]
name = (os.path.basename(mp4_file)).split(".")[0]

mp3_file = f"{export}//{name}.mp3"

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file, logger=None)
audioclip.close()
videoclip.close()

sys.exit(0)
