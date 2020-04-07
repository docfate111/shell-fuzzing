#!/bin/bash
pip3 install gramfuzz
#pip install gramfuzz
mkdir /home/tests/testscripts
for x in {1..15}
do
    python3 main.py >> '/home/tests/testscripts/script'$x'.sh'
done
