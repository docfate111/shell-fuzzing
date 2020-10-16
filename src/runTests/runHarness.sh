#!/bin/sh
mkdir -p ~/smoosh-fuzz/results
afl-fuzz -i ~/smoosh-fuzz/seeds -o ~/smoosh-fuzz/results ./harness @@