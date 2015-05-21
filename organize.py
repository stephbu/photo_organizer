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

__author__ = "stephbu"

import os
import folderutils
import exifextractor
import sys

def by_date(source_folder, output_folder = None):

	if(not os.path.isdir(source_folder)):
		raise IOError

	if(not output_folder is None):
		if(not os.path.isdir(output_folder)):
			raise IOError
	else:
		output_folder = source_folder
	
	print "reading from", output_folder
		
	for filename in folderutils.enumerate(source_folder, "NEF"):
		
		photo_date = exifextractor.dateshot(filename)
		foldername = os.path.join(output_folder, folderutils.generate_folder(photo_date))
		
		print filename, foldername
	
arg_count = len(sys.argv)

if(arg_count < 2 and arg_count > 3):
	raise ValueError	

source_folder = sys.argv[1]
output_folder = sys.argv[2] if arg_count == 3 else None

print source_folder, output_folder

by_date(source_folder, output_folder)