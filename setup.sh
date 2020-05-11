#!/bin/bash
docker build --network=host -t shellfuzz setup
#run but not as root so we can run afl-fuzz
docker run --user=newuser -it shellfuzz:latest
