# photo_organizer

Basic python tools to organize large directories full of NIKON .NEF images into folders named by EXIF DateTimeOriginal tag

## NEF EXIF Data
I use Tag #306 DateTimeOriginal to determine the camera source date taken.  This encoded string omits timezone information and is formatted as:

  <code>
  YYYY:mm:dd HH:MM:SS
  </code>
  
While developing the code, I discovered that the NEF tags don't appear to encode the Timezone information (Tag #34858 - TimezoneOffset)
even though the camera is explicitly set for the timezone (determines it's Local TZ).  Workarounds suggested parsing GPS data if it was available.  I've not had a chance to try that out yet, so I ended up with an 
assumption that the NEF data is encoded in Local Timezone format.

## Output Folder Structure
The code copies or moves the file without altering the original

  <code>
  YYYY/mm-dd/<original-filename>.NEF
  </code>
