FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y git xz-utils wget autotools-dev automake perl man groff-base cmake libncurses5-dev \
    python3 make python3-pip build-essential sudo libreadline-dev gettext ninja-build autoconf software-properties-common bison flex && \
    #ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
    #dpkg-reconfigure --frontend noninteractive tzdata && \
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
  # asciidoc
    pip3 install termcolor gramfuzz && \
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
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata asciidoc
WORKDIR /home
RUN git clone https://github.com/mgree/smoosh-fuzz.git && \
    cd smoosh-fuzz/src/scriptGeneration && \
    ./generateScripts.sh 50
WORKDIR /home/smoosh-fuzz/shells
#   b. A bunch of shells. At a minimum:
#      - dash
RUN  git clone https://salsa.debian.org/debian/dash.git && \
      cd dash && \
     CC=$(which afl-gcc) ./configure --without-tcsetpgrp  && make && make install && cd /home/smoosh-fuzz/shells && \
#     - tcsh
     git clone https://salsa.debian.org/debian/tcsh.git && \
     cd tcsh && \
     CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure --without-tcsetpgrp  && make install &&  cd /home/smoosh-fuzz/shells && \
#      - zsh
     git clone https://salsa.debian.org/debian/zsh.git && cd zsh && \
     CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure --without-tcsetpgrp  && make install &&  cd /home/smoosh-fuzz/shells && \
#WORKDIR /home/smoosh-fuzz/shells
#      - yash
    git clone https://salsa.debian.org/debian/yash.git && cd yash && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  && make install && cd /home/smoosh-fuzz/shells && \
#WORKDIR /home/smoosh-fuzz/shells
#      - ksh
#    git clone https://salsa.debian.org/debian/ksh.git && cd ksh  && CC=$(which afl-gcc) ninja -C build install &&  cd /home/smoosh-fuzz/shells && \
#      - mksh
    git clone https://evolvis.org/anonscm/git/alioth/mksh.git -b master && cd mksh &&  CC=$(which afl-gcc) /bin/sh ./Build.sh && cp mksh /usr/local/bin/mksh && cd /home/smoosh-fuzz/shells && \
#WORKDIR /home/smoosh-fuzz/shells
#      - bosh: afl gives error when running ./bosh
    git clone https://salsa.debian.org/carnil/bosh.git && cd bosh && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  && make && make install &&  cd /home/smoosh-fuzz/shells && \
#WORKDIR /home/smoosh-fuzz/shells
#      - fish: error about fish being slow from afl-fuzz
    git clone https://salsa.debian.org/debian/fish.git && cp -r fish /usr/local/fish && cd /usr/local/fish && \
    mkdir build; cd build && CC=$(which afl-gcc) CCX=$(which afl-g++) cmake .. && CC=$(which afl-gcc) CCX=$(which afl-g++) make && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) make install &&  cd /home/smoosh-fuzz/shells
    #bash version 5 errors getting bash 5
    #git clone https://salsa.debian.org/debian/bash.git && CC=$(which afl-gcc) CCX=$(which afl-g++) make && \
    #cp bash bash5 && cp bash5 /usr/local/bin/bash5
WORKDIR /home/smoosh-fuzz/shells
#      - bash (3.x (MAC) and  4.x)
RUN tar -xf bash-4.0.tar.gz && \
    tar xf bash-3.2.57.tar.gz && \
    cd bash-4.0 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  &&  CC=$(which afl-gcc) CCX=$(which afl-g++) make && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) make install && cp bash /usr/local/bin/bash4 && cd /home/smoosh-fuzz/shells && \
    cd bash-3.2.57 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  && CC=$(which afl-gcc) CCX=$(which afl-g++) make && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) make install && cp bash /usr/local/bin/bash3
WORKDIR /home/smoosh-fuzz/shells
#      - heirloom SH
RUN git clone https://github.com/grml/heirloom-sh && \
    cd heirloom-sh/ && \
      CC=$(which afl-gcc) CCX=$(which afl-g++) make && mv sh /usr/local/bin/heirloom-sh &&  cd /home/smoosh-fuzz/shells && \
    tar -x --xz < oil-0.8.pre4.tar.xz && \
    cd oil-0.8.pre4 && \
    CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  && CC=$(which afl-gcc) CCX=$(which afl-g++) make && ./install \
    && cd /home/smoosh-fuzz/shells/ && rm *gz *xz
WORKDIR /home/smoosh-fuzz/shells
# for some reason this gives an error:
# maybe later posh shell could be tested
# RUN apt source posh && cd posh && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && make && make install
WORKDIR /home/smoosh-fuzz/shells
RUN mkdir -p /home/tests/zshtests && cp -r zsh/Test/* /home/tests/zshtests && \
    mkdir -p /home/tests/yashtests &&  cp -r yash/tests/* /home/tests/yashtests && \ 
    mkdir -p /home/tests/tcshtests &&  cp -r tcsh/tests/* /home/tests/tcshtests && \ 
    mkdir -p /home/tests/mkshtests && cp -r mksh/test.sh /home/tests/mkshtests && \
    mkdir -p /home/tests/fishtests && cp -r fish/tests/* /home/tests/fishtests && \ 
    mkdir -p /home/tests/bash4tests && cp -r bash-4.0/tests/* /home/tests/bash4tests && \ 
    mkdir -p /home/tests/bash3tests && cp -r bash-3.2.57/tests/* /home/tests/bash3tests && \
    touch ~/.zshrc && mkdir -p /home/tests/results && \
    mkdir -p /home/tests/alltests && cp -r yash/tests/* /home/tests/alltests && \ 
    cp -r zsh/Test/* /home/tests/alltests && \
    cp -r yash/tests/* /home/tests/alltests && \
    cp -r tcsh/tests/* /home/tests/alltests && \
    cp -r mksh/test.sh /home/tests/alltests && \
    cp -r fish/tests/* /home/tests/alltests && \
    cp -r bash-4.0/tests/* /home/tests/alltests && \
    cp -r bash-3.2.57/tests/* /home/tests/alltests && \
    python3 /home/smoosh-fuzz/src/runTests/checkInstall.py
  #cp /home/tests/testscripts/* /home/tests/smoosh-fuzz/tests
# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.