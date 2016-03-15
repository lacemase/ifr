import sys, re, os, os.path, csv


outdir = r"E:\GLAHF_master\database\temperature_energy_climate\thermocline_depth\processed\jbreck_script\for_ken\data"


errorfile = open(os.path.join(outdir, "error.csv"), "w")


# Because we might want to flag input rows that are missing data, we need
#  to write out the error file header line before we start reading the
#  input file.  
print >>errorfile, '"Profile_ID","Error_Code","Error_Level","Error_Description"'


i = 0

if i > 1:
    i = i + 1
else: 
    print "Error!"
    print >>errorfile, '"1", "N/A", i, "i is less than 1"'

errorfile.close()
