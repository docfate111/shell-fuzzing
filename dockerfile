FROM ubuntu:18.04
RUN apt-get update -y && \
      apt-get install -y sudo
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git python3 python3-pip build-essential libreadline-dev software-properties-common && \
    apt-get upgrade -y

#1. Write a docker that sets up
#   a. random generation script
RUN mkdir -p /var/www/tests
WORKDIR /var/www/tests
RUN git clone https://github.com/mgree/smoosh-fuzz.git
RUN cd smoosh-fuzz/src
CMD generateScripts.sh
#   b. A bunch of shells. At a minimum:
RUN apt-add-repository -y ppa:fish-shell/release-3
RUN apt-get update -y && apt-get upgrade -y
#      - dash
#      - yash
#      - ksh
#      - mksh
#      - bosh
#      - zsh
#      - fish
RUN apt-get install -y bash dash yash ksh mksh bosh zsh fish
#      - bash (3.x, 4.x, and 5.x)
RUN git clone https://github.com/MacMiniVault/bash3.2.53.git
RUN bash3='/bash3.2.53/bin/bash'
#bash 4.4
RUN git clone https://github.com/gitGNU/gnu_bash.git
RUN cd gnu_bash
CMD configure
CMD make
WORKDIR /var/www/tests
#bash 5.0
RUN git clone https://github.com/errodriguez/bash5.git
RUN cd bash5
CMD configure
CMD make
WORKDIR /var/www/tests
#      - osh
#RUN git clone https://github.com/oilshell/oil.git
#RUN cd oil
#RUN git submodule update --init --recursive
#RUN osh=~/oil/bin/osh
#WORKDIR /var/www/tests
#      - heirloom SH
RUN git clone https://github.com/Sunshine-OS/heirloom-sh.git
RUN cd heirloom-sh
CMD make
CMD make install
WORKDIR /var/www/tests
# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.
