# 
# Written By:   Lacey Mason
# Code Steward: Lacey Mason
# Date Created: 11MAY2015
#
# Project:  Great Lakes Aquatic Habitat Framework (GLAHF)
# Purpose:  Re-format Nalepa benthos data table
#           
#
# Python version 2.7
#

# Import system modules
import sys, os, os.path, time, csv

# Print system start time and date
tstart = time.strftime('%X %x %Z')
print tstart


########################SET CODE PARAMETERS#################################
# Input File Name
inputPath  = r"E:\GLAHF_master\database\biological\NOAA_GLERL\for_BSJ\sgb8796_bySPP_DesitybySeason.csv"

# Output File Name
outputPath = r"E:\GLAHF_master\database\biological\NOAA_GLERL\for_BSJ\sgb8796_bySPP_DesitybySeason_altered.csv"


###########################################################################

# Create an empty list to store rows of output data
outData = list()

# Open input filename & read in file
with open(inputPath, 'rb') as F :
    csvIn = csv.reader(F, delimiter=',')

    # Read through each row in the file
    for row in csvIn :
        # Assign header row to a list
        if row[0] == "UNQSampleID":
            inHeaderRow = list()
            for h in row :
                inHeaderRow.append(h)
        else :
            # Assign values from each column to a variable and write a row to the list "outData"
            UNQSampleID = row[0]
            SEASON = row[1]
            Year = row[2]
            GLAHFSTID = row[3]
            STATION = row[4]
            
            for i in range(5, 155) :
                outData.append([UNQSampleID, SEASON, Year, GLAHFSTID, STATION, row[i], inHeaderRow[i]])

print len(outData)        
    


# Open a new csv file to write the reformatted data rows
with open(outputPath, 'wb') as H :
    csvOut = csv.writer(H, delimiter=',')
    headerRow = ["UNQSampleID", "SEASON", "Year", "GLAHFSTID", "STATION", "DENSITY", "SPECIES"]
    csvOut.writerow(headerRow)
    # Write each list in outData to the output file
    for Y in range(len(outData)):
        csvOut.writerow([z for z in outData[Y]])








# Print system end time and date
print "End of processing."
tend = time.strftime('%X %x %Z')
print tend
