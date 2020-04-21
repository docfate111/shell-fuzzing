#!/bin/bash
docker build -t testingbox setup
docker run -it testingbox:latest
