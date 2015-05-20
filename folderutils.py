import glob
from datetime import datetime

def generate_foldername(source_date):
    
    date_part = source_date.date()
    
    year = date_part.year
    month = date_part.month
    day = date_part.day
    
    path = "{0:04d}/{1:02d}-{2:02d}".format(year, month, day)
    
    return path
    
def enumerate_NEF(source_folder)

    search_path = os.path.join(source_folder, "*.NEF")
    return glob.iglob(search_path)