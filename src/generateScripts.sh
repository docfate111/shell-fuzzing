#!/bin/bash
pip3 install gramfuzz
mkdir testscripts
chmod 777 testscripts
for x in {1..15}
do
    touch 'testscripts/script'$x'.sh'
    python3 main.py >> 'testscripts/script'$x'.sh'
done
