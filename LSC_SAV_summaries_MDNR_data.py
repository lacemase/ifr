# 
# Written By:   Lacey Mason
# Code Steward: Lacey Mason
# Date Created: 17NOV2014
#
# Project:  Great Lakes Aquatic Habitat Framework
# Purpose:  
#
# Python version 2.7
#

# Import modules
import os, time
import struct, numpy, csv
#from scipy import stats

# Print system start time and date
tstart = time.strftime('%X %x %Z')
print tstart



########################SET CODE PARAMETERS#################################
# Input Folder
inputFolder = r"C:\MDNR_SAV_LSC\processed\tables\CSV"

# Output Folder & File Name
outputFolder = r"C:\MDNR_SAV_LSC\processed\SAV_summaries"

# Specify years of data to include
yearmin = 2008
yearmax = 2011

############################################################################
allDataList = list()
yearList = list()

for item in os.listdir(inputFolder) :
    # Read only the files that end with .csv
    if item.endswith('.csv'):
            inputPath = os.path.join(inputFolder, item)
            # Read in the list of stations
            if item.startswith('Station') :
                # Create list of the station location information
                StationList = list()
                with open(inputPath, 'rb') as F:
                    for line in F :
                        fields = line.split()
                        StationList.append(fields)
                        
            # Read in each table of SAV data
            else :           
                year = int(item.split(".csv")[0].split("_")[0])
                
                #### Specify the year range ####
                if year >= yearmin and year <= yearmax :
                    print item, year

                    # Create a list to hold each variable of interest
                    
                    with open(inputPath, 'rb') as F:
                        for line in F :
                            if line.startswith("report") : continue
                            fields = line.split()
                            allDataList.append(fields)
                        print 'length master list:', len(allDataList)


# Create list to store final stats
statList = list()

# Loops through the list of stations
for element in StationList :
    if element[0].startswith("Station") : continue
    staID = int(element[0][0:3])
    #print staID
    staLat = float(element[0].split(",")[1])
    staLon = float(element[0].split(",")[2])

    # For each station, creates a new list for each variable of interest
    depthList = list()
    plantTopList = list()
    perCoverList = list()
    # biovolume: percent of water column inhabitated by plant canopy
    bioVolList = list()

    # For every sonar record across all years of interest, compiles
    # data one station at a time
    for each in allDataList :
        staID_2 = int(each[0].split(",")[-1])

        # Some years have a '0' for one of the station ID's
        if staID_2 == 0 :
            #print 'staID = 0'
            continue
        
        if staID_2 == staID :
            depthList.append(float(each[0].split(",")[5]))
            plantTopList.append(float(each[0].split(",")[6]))
            perCoverList.append(float(each[0].split(",")[7]))
            bioVolList.append(float(each[0].split(",")[15]))
        else : continue

    # If the list for each variable is not empty, calculate the average value        
    if depthList != [] :
        meanDepth = numpy.mean(depthList)
    else : continue

    if plantTopList != [] :
        meanPlantTop = numpy.mean(plantTopList)
    else : continue

    if perCoverList != [] :
        meanCover= numpy.mean(perCoverList)
    else : continue

    if bioVolList != [] :
        meanBioVol = numpy.mean(bioVolList)
    else : continue

##    print 'mean depth for station', staID, 'is', meanDepth
##    print 'mean plantTop for station', staID, 'is', meanPlantTop
##    print 'mean percent cover for station', staID, 'is', meanCover
##    print 'mean bio-Volume for station', staID, 'is', meanBioVol
    
    statList.append([staID, staLat, staLon, meanDepth, meanPlantTop, meanCover,
                     meanBioVol])
    #print 'statList is', statList


# Open a new csv file to write the calculated statistics
outputFilename = "LSC_SAV_station_summary" + '_' + str(yearmin) + '_' + str(yearmax) + ".csv"
outputPath = os.path.join(outputFolder, outputFilename)
with open(outputPath, 'wb') as J :
    csvOut = csv.writer(J, delimiter=',')
    # Write header row to output file
    csvOut.writerow(["StationID", "Lat", "Lon", "mean_depth_m", "avg_plant_top_m",
                     "mean_per_cover", "mean_per_bio_vol"])
    # Write each list in statList to the output file
    for Y in range(len(statList)):
        csvOut.writerow([z for z in statList[Y]])

    

# Print system end time and date
print "End of processing."
tend = time.strftime('%X %x %Z')
print tend
