#!/usr/bin/env python3

solutions = []
for x in range(1, 22):
    for y in range(13):
        a = x * 22**4 + 2 * 22**3 + 3 * 22**2 + x * 22 + 5
        b = 6 * 13**4 + 7 * 13**3 + y * 13**2 + 9*13 + y
        if (a - b) % 57 == 0:
            solutions.append((x + y, (a - b) // 57))

print(min(solutions)[1])
