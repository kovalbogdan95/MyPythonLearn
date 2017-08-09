# NEVE RUN THIS
# Im not joking!
# ;)
import os, random

for files in range(0, 1000000):
    fname = "file" + str(random.randrange(1, 100000000)) + ".txt"
    fhand = open(fname, "w")
    fhand.write("test")
    fhand.close()