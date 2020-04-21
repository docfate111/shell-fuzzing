#!/bin/bash
docker build -t testingbox setup/Dockerfile
docker run -it testingbox:latest
