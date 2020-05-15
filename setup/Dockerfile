FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    EBIAN_FRONTEND="noninteractive" apt-get install -y git xz-utils wget gettext autoconf asciidoc ninja-build libncurses5-dev nodejs npm \
    python3 make python3-pip build-essential libreadline-dev software-properties-common tmux nano && \
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    #1. Write a docker that sets up
#   a. random generation script
    # mkdir -p /home/tests && \
    # mkdir -p /home/results && \
    # mkdir -p /home/results/zsh && \
    # mkdir -p /home/results/yash && \
    # mkdir -p /home/results/bosh && \
    # mkdir -p /home/results/mksh && \
    # mkdir -p /home/results/fish && \
    # mkdir -p /home/results/bash5 && \
    # mkdir -p /home/results/bash3 && \
    # mkdir -p /home/results/bash4 && \
    # mkdir -p /home/results/ksh && \
    # mkdir -p /home/results/dash && \
    # mkdir -p /home/results/heirloomsh && \
    # mkdir -p /home/results/osh && \
  #  chmod 777 /home/results/* && \
    npm install -g npm && \
    npm init --yes && \
    npm install command-exists colors shelljs.exec && \
    groupadd --gid 5000 newuser && \
    useradd --home-dir /home/newuser --create-home --uid 5000 \
    --gid 5000 --shell /bin/sh --skel /dev/null newuser && \
    git clone https://github.com/google/AFL.git && \
    cd AFL && \
    make && \
    make install && \
    make clean all && \
    CC=/usr/local/bin/afl-g++ && \
    CCX=/usr/local/bin/afl-gcc && \
    #so we can use apt source
    cp /etc/apt/sources.list /etc/apt/sources.list~ && \
    sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list && \
    apt update
WORKDIR /home
RUN git clone https://github.com/mgree/smoosh-fuzz.git && \
    cd smoosh-fuzz/src/scriptGeneration && \
    ./generateScripts.sh 50
WORKDIR /home/smoosh-fuzz/shells
#   b. A bunch of shells. At a minimum:
#      - dash
RUN  apt source dash && \
     cd dash-0.5.10.2 && \
     CC=$(which afl-gcc) ./configure && make && make install && cd .. && \
#WORKDIR /home/smoosh-fuzz/shells
#     - tcsh
    apt source tcsh && \
    cd tcsh-6.21.00 && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && make install && \
#WORKDIR /home/smoosh-fuzz/shells
#      - zsh
    apt source zsh && cd zsh-5.8 && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && make install && \
#WORKDIR /home/smoosh-fuzz/shells
#      - yash
    apt source yash && cd yash-2.49 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && make install && cd .. && \
#WORKDIR /home/smoosh-fuzz/shells
#      - ksh
    apt source ksh && cd ksh-2020.0.0  && CC=$(which afl-gcc) ninja -C build install && cd .. && \
#WORKDIR /home/smoosh-fuzz/shells
#      - mksh
    apt source mksh && cd mksh-58 &&  CC=$(which afl-gcc) /bin/sh ./Build.sh && cp mksh /usr/local/bin/mksh \
#WORKDIR /home/smoosh-fuzz/shells
#      - bosh: afl gives error when running ./bosh
    apt source bosh && cd bosh-0.6 CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && make install && cd .. && \
#WORKDIR /home/smoosh-fuzz/shells
#      - fish: error about fish being slow from afl-fuzz
    apt source fish && cp -r fish-3.1.0 /usr/local/fish && cd /usr/local/fish && \
    mkdir build; cd build && CC=$(which afl-gcc) CCX=$(which afl-g++) cmake .. && CC=$(which afl-gcc) CCX=$(which afl-g++) make && CC=$(which afl-gcc) CCX=$(which afl-g++) make install && \
    #bash version 5
    apt source bash && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && CC=$(which afl-gcc) CCX=$(which afl-g++) make && \
    cp bash bash5 && cp bash5 /usr/local/bin/bash5
WORKDIR /home/smoosh-fuzz/shells
#      - bash (3.x (MAC) and  4.x)
RUN tar -xf bash-4.0.tar.gz && \
    tar xf bash-3.2.57.tar.gz && \
    cd bash-4.0 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure &&  CC=$(which afl-gcc) CCX=$(which afl-g++) make && CC=$(which afl-gcc) CCX=$(which afl-g++) make install && cd .. && \
    cd bash-3.2.57 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && CC=$(which afl-gcc) CCX=$(which afl-g++) make && CC=$(which afl-gcc) CCX=$(which afl-g++) make install
WORKDIR /home/smoosh-fuzz/shells
#      - heirloom SH
RUN git clone https://github.com/grml/heirloom-sh && \
    cd heirloom-sh/ && \
      CC=$(which afl-gcc) CCX=$(which afl-g++) make && mv sh /usr/local/bin/heirloom-sh && cd .. && \
    tar -x --xz < oil-0.8.pre4.tar.xz && \
    cd oil-0.8.pre4 && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && CC=$(which afl-gcc) CCX=$(which afl-g++) make && ./install
  #cp /home/tests/testscripts/* /home/tests/smoosh-fuzz/tests
#RUN node /home/tests/smoosh-fuzz/src/runTests/checkInstall.js
# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.
