#!/usr/bin/env zsh
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-06-05 15:33:23 (UTC+0200)

DIRSCRIPT="$(dirname "$(readlink -f "$0")")"
"$DIRSCRIPT/np.py" "$1"
