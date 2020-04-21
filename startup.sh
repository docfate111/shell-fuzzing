#!/bin/bash
docker build -t testingbox .
docker run -it testingbox:latest
