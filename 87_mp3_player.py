""" 87**Mp3 Player**
    A simple program for playing your favorite music files. Add features you though are missing from
    your favorite music player.
"""
from mplayer import Player, CmdPrefix

# set default prefix for all Player instances
Player.cmd_prefix = CmdPrefix.PAUSING_KEEP

# since autospawn is True by default, no need to call player.spawn() manually
player = Player()

# play a file
player.loadfile('file.mp3')

# pause playback
player.pause()

# get title from metadata
metadata = player.metadata or {}
print(metadata.get('Title', ''))

# print the filename
print(player.filename)

# seek +5 seconds
player.time_pos += 5

# set to fullscreen
player.fullscreen = True

# terminate MPlayer
player.quit()