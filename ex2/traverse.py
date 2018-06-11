# directory traversing with recurrsion

import os.path
import glob


def traverse(base=".", depth=0):
    base = os.path.normpath(base)
    print('  '*depth + '|--', os.path.basename(base))
    if os.path.isdir(base):
        for i in glob.iglob(base+'/*'):
            traverse(i, depth+1)


if __name__ == "__main__":
    print('Current working directory:', os.getcwd())
    # traverse("..\\")
    traverse(".")
