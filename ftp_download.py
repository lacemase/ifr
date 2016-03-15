# 
# Written By:   Lacey Mason
# Code Steward: Lacey Mason
# Date Created: 25Jan2013
#
# Project:  Great Lakes Aquatic Habitat Framework
# Purpose:  Download data from FTP link
#
# Python version 2.7
#

# Import modules
import ftplib, os, time
from ftplib import FTP


# Print system start time and date
tstart = time.strftime('%X %x %Z')
print tstart


########################SET CODE PARAMETERS#################################
# Set folder path where downloaded files will be saved
outputFolder = r"E:\raw_data\2013"

# This is the base that the URLs are relative to... minus the year:
ftpbegin = "coastwatch.glerl.noaa.gov"
ftpend = "/glsea/glsea2/asc/2012"


#############################################################################

# Open FTP connection and login
ftp = FTP(ftpbegin)
ftp.login("anonymous", "lmas@umich.edu")

# Change FTP directory to location of files
ftp.cwd(ftpend)

# List contents of directory to be downloaded
listing = list()
ftp.retrlines("LIST", listing.append)

# Create a list of filenames to download
filenames = list()
for item in listing :
    item_name = item.split(" ")[-1]
    if item_name.endswith(".asc"): filenames.append(item_name)

# Download the files
for filename in filenames :
    print "Downloading " + filename
    local_filename = os.path.join(outputFolder, filename)
    if os.path.exists(local_filename) :
        print "Already downloaded " + filename
        continue
    else :
        lf = open(local_filename, "wb")
        ftp.retrbinary("RETR " + filename, lf.write)
        lf.close()


# Print system end time and date
print "End of processing."
tend = time.strftime('%X %x %Z')
print tend
