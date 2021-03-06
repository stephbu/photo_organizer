#!/usr/bin/env python
# organize.py - (c)2015 stephbu
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Main routine for organizing photos in folders"""

__author__ = "stephbu"

import os
import shutil
import sys

import folderutils
import exifextractor


def main(args):

    arg_count = len(args)

    if 1 > arg_count > 2:
        raise ValueError

    source = args[0]
    output = args[1] if arg_count == 2 else None

    print source, output

    by_date(source, output)


def by_date(source_folder, output_folder=None):
    """
    Organize NEF files in folder by DateTimeOriginal EXIF data
    :param source_folder: str
    :param output_folder: str
    """

    if not os.path.isdir(source_folder):
        raise IOError

    if not output_folder is None:
        if not os.path.isdir(output_folder):
            raise IOError
    else:
        output_folder = source_folder

    print "reading from", output_folder

    for source_directory, source_file in folderutils.enumerate_files(source_folder, ("NEF","JPG")):
        
        source_filename = source_file[len(source_directory) + 1:]
        photo_date = exifextractor.dateshot(source_file)
        timestamped_folder = os.path.join(output_folder, folderutils.generate_folder(photo_date))

        destination_file = os.path.join(timestamped_folder, source_filename)        
        if source_file == destination_file:
            continue
        
        folderutils.ensure_dir(destination_file)
        shutil.move(source_file, destination_file)     
                
        print source_file, destination_file


if __name__ == "__main__":
   main(sys.argv[1:])
