#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Corbin Creech"

import re
import os
import sys
import shutil
import subprocess
import argparse



def get_special_paths(dirname):
    # Produces a list of files that contain the pattern 
    # and prints them on their own lines
    path_list = []
    pattern = re.compile(r'__\w+__')
    for path in os.listdir(dirname):
        full_path = os.path.abspath(path)
        if pattern.search(full_path):
            path_list.append(full_path)
    print(path_list)
    return '\n'.join(path_list)


def copy_to(path_list, dest_dir):
    # Creates a new named directory and copies the files 
    # in the file list to the new directory
    os.makedirs(dest_dir)
    for files in path_list:
        shutil.copy(files, dest_dir)


def zip_to(path_list, dest_zip):
    # Zips the files in path_list into a new .zip folder
    abspaths = '\n'.join(path_list)
    print(
        """Command im going to do:
        zip -j """ + dest_zip + ' ' + abspaths
    )
    for path in path_list:
        subprocess.Popen(['zip', '-j', dest_zip, path])
    


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--from_dir', help='name of dir to search')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    from_dir = ns.from_dir
    to_dir = ns.todir
    to_zip = ns.tozip

    if to_dir:
        path_list = get_special_paths(from_dir).split('\n')
        copy_to(path_list, to_dir)
    elif to_zip:
        path_list = get_special_paths(from_dir).split('\n')
        zip_to(path_list, to_zip)
    else:
        get_special_paths(from_dir)
    



if __name__ == "__main__":
    main(sys.argv[1:])
