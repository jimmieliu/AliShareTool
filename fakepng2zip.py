import os
import sys


path = sys.argv[1]
fout = path[:-4]

fh = bytearray(open(path, "rb").read())
fh[0] = 80
fh[1] = 75
fh[2] = 3
fh[3] = 4

fout = open(fout, "wb")
fout.write(fh)
fout.close()
