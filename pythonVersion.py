import sys
print (tuple(sys.version_info))

try:
    raw_input()
except NameError:
    input()