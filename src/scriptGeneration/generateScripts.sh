#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo 'Usage: '$0' [number of scripts to generate]'
    exit 1
fi
pip install gramfuzz
#python3-pip install gramfuzz
mkdir /home/tests/testscripts
#installs gramfuzz, makes directory to hold the test scripts,
#and makes as many scripts as the argument provided
for x in $(seq "$1")
do
    python main.py >> '/home/tests/testscripts/script'$x'.sh'
done
