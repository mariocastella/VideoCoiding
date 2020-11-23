import subprocess
import os
import tempfile
import re

filepath = "bbb_sunflower_1080p_30fps_normal.mp4"
tmpf = tempfile.NamedTemporaryFile()
os.system("ffmpeg -i \"%s\" 2> %s" % (filepath, tmpf.name))
lines = tmpf.readlines()
tmpf.close()

for l in lines:
    l = str(l.strip())
    if l.startswith('b\'Duration:'):
        start = l.find("D")
        Ginfo = l[start:-1]
    if l.startswith('b\'Stream #0:0'):
        start = l.find(")") + 3
        stream0 = l[start:-1]
    if l.startswith('b\'Stream #0:1'):
        start = l.find(")") + 3
        stream1 = l[start:-1]

print(Ginfo + "\n" + stream0 + "\n" + stream1)
