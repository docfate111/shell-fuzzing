FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git nodejs npm python python-pip build-essential libreadline-dev software-properties-common && \
    apt-add-repository -y ppa:fish-shell/release-3 && \
#1. Write a docker that sets up
#   a. random generation script
    mkdir -p /home/tests && \
    npm install -g npm && \
    npm install command-exists colors && \
    apt-get update -y && \
    apt-get upgrade -y 
WORKDIR /home
RUN git clone https://github.com/mgree/smoosh-fuzz.git && \
    cd smoosh-fuzz/src/scriptGeneration && \
    ./generateScripts.sh 15 && \
#   b. A bunch of shells. At a minimum:
#      - dash
#      - yash
#      - ksh
#      - mksh
#      - bosh
#      - zsh
#      - fish
   apt install -y bash dash yash ksh mksh bosh zsh fish && \
#      - bash (3.x, 4.x, and 5.x)
   git clone https://github.com/MacMiniVault/bash3.2.53.git && \
   cp /home/bash3.2.53/bin/bash /usr/local/bin/bash3 && \
  #bash 4.4
  git clone https://github.com/gitGNU/gnu_bash.git && \
  cd gnu_bash && \
  ./configure && \
  make
COPY bash /usr/local/bin/bash4
WORKDIR /home/tests
#bash 5.0
RUN git clone https://github.com/errodriguez/bash5.git && \
    cd bash5 && \
    ./configure && \
    make
COPY bash /usr/local/bin/bash5
WORKDIR /home/tests
#      - heirloom SH
RUN git clone https://github.com/grml/heirloom-sh && \
    cd heirloom-sh/ && \
    make
COPY sh /usr/local/bin/heirloom-sh
WORKDIR /home/tests
#    - osh isnt working
RUN git clone https://github.com/oilshell/oil.git && \
 cd oil && \
 git submodule update --init --recursive
COPY osh /usr/local/bin/osh
WORKDIR /home/tests
RUN node /home/tests/src/runTests/checkInstall.js
# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.
