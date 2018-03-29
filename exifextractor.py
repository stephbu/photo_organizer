# exifextractor.py - (c)2015 stephbu
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

"""Functions and helpers for extracting EXIF information from image files"""

__author__ = "stephbu"

import os
import time
import platform
from datetime import datetime
from dateutil import tz
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

EXIF_MODIFYDATE = 306

# 0x9003
EXIF_DATETIMEORIGINAL = 36867

# 0x9004
EXIF_CREATEDATE = 36868
LOCAL_TZ = tz.tzlocal()


def dateshot(filename):

    """
    Extract DateTimeOriginal EXIF Tag data from specified filename
    :param filename: str
    :rtype : datetime
    """

    assert isinstance(filename, str)

    if not os.path.isfile(filename):
        raise IOError

    img = Image.open(filename)

    if isinstance(img, JpegImageFile):
        exif = img._getexif()
    else:
        exif = img.tag

    localdateshottag = None
    # More robust handling of sourcing dates from different fields
    if exif and exif.has_key(EXIF_CREATEDATE):
        localdateshottag = exif.get(EXIF_CREATEDATE)

    if exif and (localdateshottag is None) and exif.has_key(EXIF_DATETIMEORIGINAL):
        localdateshottag = exif.get(EXIF_DATETIMEORIGINAL)

    if exif and (localdateshottag is None) and exif.has_key(EXIF_MODIFYDATE):
        localdateshottag = exif.get(EXIF_MODIFYDATE)

    # fallback and try to get the filesystem created or last modified dates
    if localdateshottag is None:
        localdateshottag = time.strftime('%Y:%m:%d %H:%M:%S', time.gmtime(creation_date(filename)))
        print localdateshottag

    if localdateshottag is None:
        print filename
        print exif
        assert 'No data found'

    # Pillow started to return multiple value tuple for some new NEF files
    # if so, this will take only the first value to try and convert into an array
    if isinstance(localdateshottag, tuple):
        localdateshottag = localdateshottag[0]

    # Pillow NEF/TIFF parser omits tag 34858:TimeZoneOffset
    try:
        localdate = datetime.strptime(localdateshottag, '%Y:%m:%d %H:%M:%S')
    except ValueError:
        print "unable to parse tag value", localdateshottag
        raise

    localdate.replace(tzinfo=LOCAL_TZ)

    img.close()

    return localdate


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
