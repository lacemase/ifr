# 
# Written By:   Jason Breck
# Code Steward: Lacey Mason
# Date Created: 14Jun2011
#
# Project:  Great Lakes GIS
# Purpose:  Download NOAA ice data frome natice
#
# Python version 2.6
#

# Import modules
import urllib, re, shutil, os.path, time


# Print system start time and date
tstart = time.strftime('%X %x %Z')
print tstart


########################SET CODE PARAMETERS#################################
# Set folder path where downloaded files will be saved
target = r"S:\Drop_Box\DForsyth\NOAA_ice_data\data"

# This is the base that the URLs are relative to... minus the year:
urlbegin = "http://www.natice.noaa.gov/pub/special/great_lakes/"
urlend = "/daily_ice_concentration/shapefiles/"

# Years for the winter
year1 = '2010'
year2 = '2011'

# File prefix for year 1
year1prefix = 'gl10'

# String of file names from website
z="""
    gl101201_lam.zip      
gl101202_lam.zip      
gl101208_lam.zip    
gl101209_lam.zip      
gl101210_lam.zip      
gl101211_lam.zip      
gl101212_lam.zip      
gl101213_lam.zip     
gl101214_lam.zip      
gl101215_lam.zip     
gl101216_lam.zip     
gl101217_lam.zip      
gl101218_lam.zip   
gl101219_lam.zip   
gl101220_lam.zip     
gl101221_lam.zip      
gl101222_lam.zip     
gl101223_lam.zip     
gl101224_lam.zip    
gl101225_lam.zip     
gl101226_lam.zip    
gl101227_lam.zip     
gl101228_lam.zip    
gl101229_lam.zip     
gl101230_lam.zip   
gl101231_lam.zip   
gl110101_lam.zip    
gl110102_lam.zip     
gl110103_lam.zip    
gl110104_lam.zip     
gl110105_lam.zip     
gl110106_lam.zip     
gl110107_lam.zip     
gl110108_lam.zip 
gl110109_lam.zip      
gl110110_lam.zip      
gl110111_lam.zip     
gl110112_lam.zip     
gl110113_lam.zip     
gl110114_lam.zip     
gl110115_lam.zip      
gl110116_lam.zip     
gl110117_lam.zip     
gl110118_lam.zip      
gl110119_lam.zip     
gl110120_lam.zip      
gl110121_lam.zip     
gl110122_lam.zip     
gl110123_lam.zip     
gl110124_lam.zip    
gl110125_lam.zip      
gl110126_lam.zip     
gl110127_lam.zip     
gl110128_lam.zip     
gl110129_lam.zip      
gl110130_lam.zip  
gl110131_lam.zip    
gl110201_lam.zip     
gl110202_lam.zip     
gl110203_lam.zip     
gl110204_lam.zip     
gl110205_lam.zip     
gl110206_lam.zip      
gl110207_lam.zip     
gl110208_lam.zip      
gl110209_lam.zip     
gl110210_lam.zip      
gl110211_lam.zip     
gl110212_lam.zip     
gl110213_lam.zip     
gl110214_lam.zip     
gl110215_lam.zip     
gl110216_lam.zip   
gl110217_lam.zip    
gl110218_lam.zip    
gl110219_lam.zip    
gl110220_lam.zip    
gl110221_lam.zip    
gl110222_lam.zip    
gl110223_lam.zip     
gl110224_lam.zip    
gl110225_lam.zip    
gl110226_lam.zip    
gl110227_lam.zip     
gl110228_lam.zip     
gl110301_lam.zip    
gl110302_lam.zip    
gl110303_lam.zip    
gl110304_lam.zip      
gl110305_lam.zip      
gl110306_lam.zip  
gl110307_lam.zip    
gl110308_lam.zip      
gl110309_lam.zip      
gl110310_lam.zip     
gl110311_lam.zip     
gl110312_lam.zip  
gl110313_lam.zip    
gl110314_lam.zip     
gl110315_lam.zip     
gl110316_lam.zip      
gl110317_lam.zip     
gl110318_lam.zip    
gl110319_lam.zip     
gl110320_lam.zip     
gl110321_lam.zip     
gl110322_lam.zip      
gl110323_lam.zip     
gl110324_lam.zip     
gl110325_lam.zip      
gl110326_lam.zip     
gl110327_lam.zip      
gl110328_lam.zip      
gl110329_lam.zip      
gl110330_lam.zip      
gl110331_lam.zip     
gl110401_lam.zip    
gl110402_lam.zip      
gl110403_lam.zip      
gl110404_lam.zip      
gl110405_lam.zip     
gl110406_lam.zip     
gl110407_lam.zip      
gl110408_lam.zip     
gl110409_lam.zip      
gl110410_lam.zip      
gl110411_lam.zip     
gl110412_lam.zip      
gl110413_lam.zip      
gl110414_lam.zip     
gl110415_lam.zip     
gl110416_lam.zip      
gl110417_lam.zip      
gl110418_lam.zip     
gl110419_lam.zip      
gl110420_lam.zip     
gl110421_lam.zip      
gl110422_lam.zip      
gl110423_lam.zip      
gl110424_lam.zip     
gl110425_lam.zip      
gl110426_lam.zip      
gl110427_lam.zip      
gl110428_lam.zip     
gl110429_lam.zip      
gl110430_lam.zip     
gl110501_lam.zip      
gl110502_lam.zip      
gl110503_lam.zip      
gl110504_lam.zip     
gl110505_lam.zip      
gl110506_lam.zip     
gl110509_lam.zip     
gl110510_lam.zip     
gl110511_lam.zip     
gl110512_lam.zip     
gl110513_lam.zip  


"""
#############################################################################


# Code to download Files
# Find file name pattern in string
zip_expression = '\S+.zip'

all_links = list()

# Populate all_links list with the file names
all_links.extend(re.findall(zip_expression, z))

# For each file path, download the file and save to target on server
for x in all_links :
    year = year1 if year1prefix in x else year2
    urlbase = urlbegin + year + urlend
    print "Downloading " + x
    urlFilename = x.split("/")[-1]
    tempPath, headers = urllib.urlretrieve(urlbase + x)
    targetPath = os.path.join(target, urlFilename)
    shutil.move(tempPath, targetPath)


# Print system end time and date
print "End of processing."
tend = time.strftime('%X %x %Z')
print tend
