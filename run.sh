#!/bin/sh
echo 'Make sure smoosh-fuzz is home directory'
#./provision.sh
cd ~/smoosh-fuzz/shells
make all
cd ~/smoosh-fuzz
# make scripts and put them in seeds
src/scriptGeneration/generateScripts.sh
echo 'TODO: change checkInstall.py to write all files in smoosh-fuzz/shells/bin into file labelled "installed_shells"' 
cd  src/runTests
# get list of shells installed in smoosh-fuzz/shells/bin
./checkInstall.sh
# start fuzzing with the harness
./runHarness.sh
