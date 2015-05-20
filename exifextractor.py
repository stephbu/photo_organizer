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
    
