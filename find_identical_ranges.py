#!/usr/bin/env python #
"""
This script allows you to compare a bunch of files, and report on ranges that are identical across all files.

Usage: find_identical_ranges.py > output.txt
"""
import os

dir_path = "./"
file_ext = ".bin"

file_list = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(file_ext)]

with open(file_list[0], "rb") as f:
    file_size = os.path.getsize(file_list[0])
    
identical_ranges = []

for i in range(file_size):
    all_identical = True
    with open(file_list[0], "rb") as f1:
        f1.seek(i)
        byte_val = f1.read(1)

    for file_path in file_list[1:]:
        with open(file_path, "rb") as f2:
            f2.seek(i)
            if f2.read(1) != byte_val:
                all_identical = False
                break
    if all_identical:
        if not identical_ranges or (identical_ranges and i > identical_ranges[-1][1]+1):
            identical_ranges.append((i, i))
        else:
            identical_ranges[-1] = (identical_ranges[-1][0], i)

for r in identical_ranges:
    print(f"Byte range {r[0]}-{r[1]} is identical across all files.")
