#!/bin/bash
pip3 install gramfuzz
mkdir /var/www/tests/testscripts
for x in {1..15}
do
    python3 main.py >> '/var/www/tests/testscripts/script'$x'.sh'
done
