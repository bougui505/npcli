#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-05 15:23:59 (UTC+0200)

import sys
import numpy as np

data = np.loadtxt(sys.stdin, dtype=np.int)  # See: https://stackoverflow.com/a/8192426/1679629
exec(sys.argv[1])
print(data)
