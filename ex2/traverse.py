#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'shnam7'

import os.path
import glob

print('Current working directory:{}'.format(os.getcwd()))

def traverse(base=".", depth=0):
    base = os.path.normpath(base)
    print('  '*depth + '|--', os.path.basename(base))
    if os.path.isdir(base):
        for i in glob.iglob(base+'/*'):
            traverse(i, depth+1)

traverse("..\\")
