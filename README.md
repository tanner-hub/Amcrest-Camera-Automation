# Amcrest-Camera-Automation

from amcrest import AmcrestCamera
import time, sys

Check software information
camera.software_information

Capture snapshot
camera.snapshot(0, "/home/user/Desktop/snapshot00.jpeg")

Capture audio --> CTRL-C to stop the continuous audio flow or use a timer
camera.audio_stream_capture(httptype="singlepart", channel=1, path_file="/home/user/Desktop/audio.aac")

Record realtime stream into a file --> CTRL-C to stop the continuous video flow or use a timer
camera.realtime_stream(path_file="/home/user/Desktop/myvideo")
