# photo_organizer

Basic python tools to organize large directories full of NIKON .NEF and JPEG images into folders organized by picture date.
The date is extracted from EXIF metadata, in priority order as follows: CreateDate, DateTimeOriginal, ModifyDate tags, then as fallback filesystem created or last-modified attributes.

## How To Use
Fast Start
- Clone this repository
- Install dependency libraries Pillow/PIL, datetime, dateutil
- Run In The "Work In Progress" Directory e.g.
````
python ./organize.py /users/stephbu/pictures
````
- Output directories created as children of current directory

Advanced
- TBD

## Intention
This code is intend to enable me to quickly manipulate flat folders full of files into a year/month/day encoded set of folders that I can merge into my long term storage.

## Workflow
I take a lot of photos and sweep them off camera into "Work in Progress" folders until I have time to process them at a later date.  It takes less than an hour to generate more photos than you can process in one day.  When I process my photos I move them into date encoded set of folders for long term storage.

My workflow generates folder structure that look like this:
```
  photo_root/
             work_in_progress/
                              date1/
                              date2/
                              daten/
             year1/
                  month1-day1 meaningful label/
                  month2-day1 meaningful label/
             yearn/
                  month-day meaningful label/
```  
## NEF EXIF Data
Nikon's NEF format is an extension of the TIFF format. Metadata such as time, camera, lense etc. are encoded into the NEF file as EXIF data structures.  I selected Python Pillow libraries to parse the TIFF EXIF metadata for two reasons:

- Pillow is an active community-maintained EXIF library
- These tools developed on OS/X

I use Tag #306 DateTimeOriginal to determine the camera source date taken.  This encoded string omits timezone information and is formatted as:

  <code>
  YYYY:mm:dd HH:MM:SS
  </code>
  
While developing the code, I discovered that the NEF tags don't appear to encode the Timezone information (Tag #34858 - TimezoneOffset)
even though the camera is explicitly set for the timezone (determines it's Local TZ).  Workarounds suggested parsing GPS data if it was available.  I've not had a chance to try that out yet, so I ended up with an 
assumption that the NEF data is encoded in Local Timezone format.

## Output Folder Structure
The code copies or moves the file without altering the original - for a source structure

```
  sourcefolder/
              DSC0001.NEF (taken in 1/1/2014)
              subfolder1/
                        DSC0002.NEF (taken in 1/1/2014)
              subfolder2/
                        DSC0003.NEF (taken in 31/1/2014)
```  

The output would be:

```
  sourcefolder/
              2014/
                  01-01/
                    DSC0001.NEF
                    DSC0002.NEF
                  01-31/
                    DSC0003.NEF
``` 


## External Linkage
Some useful further reading on the subject
- EXIF Data http://en.wikipedia.org/wiki/Exchangeable_image_file_format
- EXIF Tag Spec http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf<br/>Tag encoding information starts on page 28.
- Pillow Source https://github.com/python-pillow/Pillow 
- NEF http://www.nikonusa.com/en/Learn-And-Explore/Article/ftlzi4ri/nikon-electronic-format-nef.html
- NEF File Format Description http://lclevy.free.fr/nef/
