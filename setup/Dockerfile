FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git xz-utils wget nodejs npm python3 python3-pip build-essential libreadline-dev software-properties-common && \
    apt-add-repository -y ppa:fish-shell/release-3 && \
#1. Write a docker that sets up
#   a. random generation script
    mkdir -p /home/tests && \
    npm install -g npm && \
      npm init --yes && \
    npm install command-exists colors shelljs.exec
WORKDIR /home/tests
RUN git clone https://github.com/mgree/smoosh-fuzz.git && \
    cd smoosh-fuzz/src/scriptGeneration && \
    ./generateScripts.sh 5 && \
#   b. A bunch of shells. At a minimum:
#      - dash
#      - yash
#      - ksh
#      - mksh
#      - bosh
#      - zsh
#      - fish
   apt install -y bash dash yash ksh mksh bosh zsh fish
#      - bash (3.x, 4.x, and 5.x)
WORKDIR /home/tests
#      - heirloom SH
RUN cd smoosh-fuzz/src && \
    git clone https://github.com/grml/heirloom-sh && \
    cd heirloom-sh/ && \
    make && mv sh /usr/local/bin/heirloom-sh
#can't do since there are errors in every bash3 version:
#RUN mv /home/smoosh-fuzz/tests/src/bash-3.0.16/bash /usr/local/bin/bash3
WORKDIR /home/tests
RUN mv smoosh-fuzz/src/bash4/bash4 /usr/local/bin/bash4 && \
    mv smoosh-fuzz/src/bash5/bash5 /usr/local/bin/bash5 && \
    cd smoosh-fuzz/src/ && \
    tar -x --xz < oil-0.8.pre4.tar.xz && \
    cd oil-0.8.pre4 && \
     ./configure && make && ./install
WORKDIR /home/tests
RUN cd smoosh-fuzz/src && rm oil-0.8.pre4.tar.xz
WORKDIR /home/tests
RUN wget http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz && \
    tar -xf afl-latest.tgz && \
    cd afl-2.52b && \
    make && \
    make install
  #cp /home/tests/testscripts/* /home/tests/smoosh-fuzz/tests
#RUN node /home/tests/smoosh-fuzz/src/runTests/checkInstall.js
# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.
