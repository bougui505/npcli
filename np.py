#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-05 15:23:59 (UTC+0200)

import sys
import numpy as np


def print(indata):
    np.savetxt(sys.stdout, indata, fmt='%.18g')


data = np.loadtxt(sys.stdin)  # See: https://stackoverflow.com/a/8192426/1679629
exec(sys.argv[1])
