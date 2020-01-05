#!/bin/bash
# since Bash v4

# If no parameter is given, ask confirmation before each rm.
if [ -z $1 ]
then
# Remove all files in output/. Asking a confirmation for each file before deleting. 
rm -i output/*

# If -nc is given (for no confirmation), rm without confirmation
elif [ $1 = "-nc" ]
then
# Remove all the .atom, .csv, .json, .json_rows, .raw, .xml and .dot in the directory output.
find output/ -regex '.*\(atom\|csv\|json\|json_rows\|raw\|xml\|dot\)$' -delete

# For all others case, ask confirmation before each rm.
else
# Remove all files in output/. Asking a confirmation for each file before deleting. 
rm -i output/*

# End if.
fi
