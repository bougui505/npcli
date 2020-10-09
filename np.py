#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-05 15:23:59 (UTC+0200)

import sys
import argparse
import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

try:
    import seaborn as sns
except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
except ImportError:
    pass


parser = argparse.ArgumentParser(description='Using python and numpy from the Shell')
parser.add_argument('--nopipe', help='Not reading from pipe', default=False, action='store_true')
parser.add_argument('-c', '--cmd', help='Command to run', type=str)
args = parser.parse_args()


def print(indata):
    if np.isscalar(indata):
        sys.stdout.write(f'{indata}\n')
    else:
        np.savetxt(sys.stdout, indata, fmt='%s')


def format_line(line):
    line = line.split()
    outline = []
    for e in line:
        try:
            e = int(float(e)) if int(float(e)) == float(e) else float(e)
        except ValueError:
            pass
        outline.append(e)
    return outline


if not args.nopipe:
    # Reading from pipe
    # data = np.genfromtxt(sys.stdin, dtype=str)  # See: https://stackoverflow.com/a/8192426/1679629
    data = []
    with sys.stdin as inpipe:
        for line in inpipe:
            line = format_line(line)
            data.append(line)
    data = pd.DataFrame(data)

exec(args.cmd)
