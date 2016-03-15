# 
# Written By:   Lacey Mason
# Code Steward: Lacey Mason
# Date Created: 18MAR2015
#
# Project:  Great Lakes Aquatic Habitat Framework (GLAHF) / CSCOR
# Purpose:  Add new sampling point locations to an existing feature class
#           
#
# Python version 2.7
#

# Import modules
import os, time, sys, csv
import arcpy
from arcpy.sa import *

# Print system start time and date
tstart = time.strftime('%X %x %Z')
print tstart

########################SET CODE PARAMETERS#################################
# Input csv file containing pre-formated point locations
incsv = r"example_input_file.csv"

# File Geodatabase file path
inGDB = r"E:\GLAHF_master\database\biological\BSJ_sample_location_update\BSJ_allSites.gdb"

# Existing Point Feature Class Name (in above named file gdb)
pointFC = r"BSJ_allSites_v12"


############################################################################

arcpy.env.workspace = inGDB

x_coords = "FinalLong"
y_coords = "FinalLat"
out_Layer = "newLocations_layer"

# Set the spatial reference
spRef = "NAD1983.prj"

print "Making XY event layer."
# Make the XY event layer...
arcpy.MakeXYEventLayer_management(incsv, x_coords, y_coords, out_Layer, spRef)


print "Appending points..."
# Append csv Events Layer to existing feature class
##arcpy.Append_management(saved_Layer, os.path.join(inGDB, pointFC), "NO_TEST", "", "")
arcpy.Append_management(out_Layer, os.path.join(inGDB, pointFC), "NO_TEST", "", "")



# Print system end time and date
print "End of processing."
tend = time.strftime('%X %x %Z')
print tend
