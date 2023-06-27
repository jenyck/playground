#!/usr/bin/env python3
from itertools import product

count = len(list(product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО')))

print(count)
