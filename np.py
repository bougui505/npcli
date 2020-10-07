#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-05 15:23:59 (UTC+0200)

import sys
import argparse
import numpy as np
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
        np.savetxt(sys.stdout, indata, fmt='%.18g')


if not args.nopipe:
    # Reading from pipe
    data = np.loadtxt(sys.stdin)  # See: https://stackoverflow.com/a/8192426/1679629
exec(args.cmd)
