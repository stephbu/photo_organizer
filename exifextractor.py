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

__author__ = "stephbu"

from PIL import Image
from datetime import datetime
from dateutil import tz

EXIF_DATE_SHOT = 306
LOCAL_TZ = tz.tzlocal()

def dateshot(filename):
    
    img = Image.open(filename)
    localDateShotTag = img.tag[EXIF_DATE_SHOT]
    
    # Pillow NEF/TIFF parser omits tag 34858:TimeZoneOffset
    try:
        localDate = datetime.strptime(localDateShotTag, '%Y:%m:%d %H:%M:%S')
    except ValueError:
        print "unable to parse tag value", localDateShotTag 
        raise
    
    localDate.replace(tzinfo = LOCAL_TZ)
    
    img.close()
    
    return localDate
    
