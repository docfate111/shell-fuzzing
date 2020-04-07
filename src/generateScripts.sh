#!/bin/bash
pip3 install gramfuzz
mkdir testscripts
chmod 777 testscripts
mv testscripts /var/www/tests
for x in {1..15}
do
    mkdir /var/www/tests/testscripts
    python3 main.py >> '/var/www/tests/testscripts/script'$x'.sh'
done
