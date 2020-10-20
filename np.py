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
parser.add_argument('-d', '--delimiter', help='Delimiter to use', type=str)
parser.add_argument('cmd', help='Command to run', type=str)
args = parser.parse_args()


def print(indata):
    try:
        indata[indata == None] = '_'
    except (TypeError, ValueError):
        pass
    if np.isscalar(indata):
        sys.stdout.write(f'{indata}\n')
    else:
        np.savetxt(sys.stdout, indata, fmt='%s', delimiter='\t')


def format_line(line):
    line = line.split(args.delimiter)
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
    # A = np.genfromtxt(sys.stdin, dtype=str)  # See: https://stackoverflow.com/a/8192426/1679629
    A = []
    with sys.stdin as inpipe:
        for line in inpipe:
            line = format_line(line)
            A.append(line)
    A = pd.DataFrame(A)
    A = np.asarray(A)
exec(args.cmd)
