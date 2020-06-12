#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-05 15:23:59 (UTC+0200)

import sys
import numpy as np
try:
    import seaborn as sns
except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
except ImportError:
    pass


def print(indata):
    if np.isscalar(indata):
        sys.stdout.write(f'{indata}\n')
    else:
        np.savetxt(sys.stdout, indata, fmt='%.18g')


data = np.loadtxt(sys.stdin)  # See: https://stackoverflow.com/a/8192426/1679629
exec(sys.argv[1])
