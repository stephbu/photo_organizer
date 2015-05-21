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
from datetime import datetime

__author__ = "stephbu"

import glob
import os


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


def enumerate_files(source_folder, extension):

    """Iterator to enumerate through source_folder and all subfolders looking for files with specified extension"""

    for root, dirs, files in os.walk(source_folder):
        for filename in glob.iglob(os.path.join(root, "*." + extension)):
            yield filename
