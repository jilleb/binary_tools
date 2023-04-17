#!/usr/bin/env python #
"""
This script allows you to display and compare binary contents from a file

Usage: list_range.py > output.txt
"""

import os
# configuration things, set these to your preference
config_startposition = 3364 # where to start 
dump_length = 16            # how much bytes would you like to list
folder_path = './'

for file_name in os.listdir(folder_path):
    if file_name.endswith('.fpa'): #modify .bin to an other extension if needed
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'rb') as f:
            start_pos = config_startposition
            end_pos = start_pos + dump_length
            length = end_pos - start_pos + 1
            f.seek(start_pos)
            bytes_list = [int.from_bytes(f.read(1), byteorder='big') for _ in range(length)]
            print(file_name, *bytes_list, sep='\t')
