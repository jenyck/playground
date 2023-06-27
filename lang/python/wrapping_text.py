#!/usr/bin/env python3
import textwrap, fileinput

for fileinput_line in fileinput.input():
    print(textwrap.fill(fileinput_line, 78))
