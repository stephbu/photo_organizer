# folderutils.py - (c)2015 stephbu
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

"""Functions to assist in folder enumeration and naming"""

__author__ = "stephbu"

import glob
import os
from datetime import datetime

def generate_folder(source_date):

    """
    Generate partial folder name based on provided source_date
    :param source_date: datetime
    """

    assert isinstance(source_date, datetime)

    date_part = source_date.date()

    year = date_part.year
    month = date_part.month
    day = date_part.day

    path = "{0:04d}/{1:02d}-{2:02d}".format(year, month, day)

    return path

def either(c):
    return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c

def enumerate_files(source_folder, extension):

    """Iterator to enumerate through source_folder and all subfolders looking for files with specified extension"""

    for root, dirs, files in os.walk(source_folder):

        if isinstance(extension, tuple):
            for ext in extension:
                for filename in glob.iglob(os.path.join(root, "*." + ''.join(either(char) for char in ext))):
                    yield root, filename
        else:
            for filename in glob.iglob(os.path.join(root, "*." + ''.join(either(char) for char in extension))):
                yield root, filename


def ensure_dir(filename):

    """Ensure directory of specified filename exists and is a directory, or is created"""

    directory = os.path.dirname(filename)

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.isdir(directory):
        raise IOError("path is file")
