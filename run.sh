#!/bin/sh
echo 'Make sure smoosh-fuzz is home directory'
mkdir -p ~/smoosh-fuzz/seeds
cd ~/smoosh-fuzz/shells
make all
cd ~/smoosh-fuzz/src/src/scriptGeneration
# make scripts and put them in seeds
./generateScripts.sh 30
cd  src/runTests
# get list of shells installed in smoosh-fuzz/shells/bin
./checkInstall.sh
# start fuzzing with the harness
./runHarness.sh
