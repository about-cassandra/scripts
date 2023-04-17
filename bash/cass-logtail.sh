#!/bin/bash

# This script is a Bash script that allows the user to tail a Cassandra log file with
# the tail command. The script has several optional flags to set the file
# location, file name, and to grep the log file for "ERROR" or "WARN". By
# default, the script tails the file /var/log/cassandra/system.log, but the
# user can override the file location and name with flags. 
# The -e flag allows the user to grep the log file for "ERROR" or "WARN".


# set default values
FILE_LOCATION="/var/log/cassandra"  # default file location
FILE_NAME="system.log"  # default file name
GREP_STRING=""  # default empty string for egrep

# function to display help instructions
function display_help {
  echo "Usage: $0 [-l FILE_LOCATION] [-n FILE_NAME] [-e]"
  echo "  -l FILE_LOCATION   Set the file location (default: /var/log/cassandra)"
  echo "  -n FILE_NAME       Set the file name (default: system.log)"
  echo "  -e                 Grep the log file for ERROR or WARN"
  echo "  -h                 Display this help message"
  exit 0
}

# parse flags
while getopts ":l:n:eh" opt; do
  case $opt in
    l)
      FILE_LOCATION=$OPTARG  # set file location
      ;;
    n)
      FILE_NAME=$OPTARG  # set file name
      ;;
    e)
      GREP_STRING="ERROR|WARN"  # set egrep string to find ERROR or WARN
      ;;
    h)
      display_help  # display help instructions and exit
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# run tail command with egrep if necessary
if [ -n "$GREP_STRING" ]; then
  tail -200f "$FILE_LOCATION/$FILE_NAME" | egrep "$GREP_STRING"  # tail the log file and grep for errors or warnings
else
  tail -200f "$FILE_LOCATION/$FILE_NAME"  # tail the log file without egrep
fi

# Disclaimer
# This script is provided "as is" and without any express or implied warranties,
# including, without limitation, the implied warranties of merchantability and
# fitness for a particular purpose. The author of this script shall not be liable
# for any damages arising from the use of this script, including, but not limited
# to, direct, indirect, incidental, punitive, and consequential damages. Use
# this script at your own risk.
