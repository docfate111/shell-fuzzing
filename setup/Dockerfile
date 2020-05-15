FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git xz-utils wget curses libintl nodejs npm python3 make python3-pip build-essential libreadline-dev software-properties-common tmux nano && \
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
    useradd --home-dir /home/newuser --create-home --uid 5000 && \
    --gid 5000 --shell /bin/sh --skel /dev/null newuser && \
    git clone https://github.com/google/AFL.git && \
    cd AFL && \
    make && \
    CCX=$(afl-g++) ./configure && \
    CC=$(which afl-gcc) ./configure &&  make clean all
WORKDIR /home/
RUN git clone https://github.com/mgree/smoosh-fuzz.git && \
    cd smoosh-fuzz/src/scriptGeneration && \
    ./generateScripts.sh 50
WORKDIR /home/smoosh-fuzz/shells
#   b. A bunch of shells. At a minimum:
#      - dash
RUN  tar xvzf dash-0.5.10.2.tar.gz && \
     cd dash-0.5.10.2 && \
     ./configure --bindir=/bin --mandir=/usr/share/man && make && \
     make install
WORKDIR /home/smoosh-fuzz/shells
#     - tcsh
RUN  tar xvzf tcsh-6.22.02.tar.gz && \
     cd tcsh-6.22.02 && \
     CFLAGS="$CFLAGS -fcommon" && \
     ./configure --prefix=/usr --bindir=/bin && \
     make && \
     sh ./tcsh.man2html && \
     ./configure --bindir=/bin --mandir=/usr/share/man && make && \
     make install && make install install.man && \
     ln -v -sf tcsh   /bin/csh && \
     ln -v -sf tcsh.1 /usr/share/man/man1/csh.1 && \
     install -v -m755 -d          /usr/share/doc/tcsh-6.22.02/html && \
     install -v -m644 tcsh.html/* /usr/share/doc/tcsh-6.22.02/html && \
     install -v -m644 FAQ         /usr/share/doc/tcsh-6.22.02
WORKDIR /home/smoosh-fuzz/shells
#      - zsh
RUN tar xvzf zsh-5.8.tar.xz && cd zsh-5.8 && \
    ./configure --prefix=/usr \
    --bindir=/bin         \
    --sysconfdir=/etc/zsh \
    --enable-etcdir=/etc/zsh && make && \
    makeinfo  Doc/zsh.texi --plaintext -o Doc/zsh.txt && \
    makeinfo  Doc/zsh.texi --html  -o Doc/html && \
    makeinfo  Doc/zsh.texi --html --no-split --no-headers -o Doc/zsh.html && \
    make install                              && \
    make infodir=/usr/share/info install.info && \
    install -v -m755 -d                 /usr/share/doc/zsh-5.8/html && \
    install -v -m644 Doc/html/*         /usr/share/doc/zsh-5.8/html && \
    install -v -m644 Doc/zsh.{html,txt} /usr/share/doc/zsh-5.8
WORKDIR /home/smoosh-fuzz/shells
#      - yash
RUN tar xvzf yash-2.49.tar.gz && ./configure && make && sudo make install
WORKDIR /home/smoosh-fuzz/shells
#      - ksh
RUN git clone https://github.com/att/ast.git && cd ast && ./bin/package make
WORKDIR /home/smoosh-fuzz/shells
#      - mksh
RUN tar xvzf mksh-R59.tgz && cd mksh-R59 && /bin/sh ./Build.sh
WORKDIR /home/smoosh-fuzz/shells
#      - bosh
RUN tar -xf bosh.tar.bz2 && cp schily-2020-05-11 bosh && rm -rf schily-2020-05-11 && \
    cd bosh && make
WORKDIR /home/smoosh-fuzz/shells
#      - fish
RUN tar -xf fish-3.1.1.tar.gz && cd fish-3.1.1 && mkdir build; cd build && \
    cmake .. && make && make install
WORKDIR /home/smoosh-fuzz/shells
#      - bash (3.x, 4.x, and 5.x) couldn't get a v3 without errors
RUN cd bash-4.0 && ./configure && make && make install && cd .. && \
    cd bash-5.0 && ./configure && make && make install
WORKDIR /home/smoosh-fuzz/shells
#      - heirloom SH
RUN git clone https://github.com/grml/heirloom-sh && \
    cd heirloom-sh/ && \
    make && mv sh /usr/local/bin/heirloom-sh
WORKDIR /home/smoosh-fuzz/shells
RUN tar -x --xz < oil-0.8.pre4.tar.xz && \
    cd oil-0.8.pre4 && \
     ./configure && make && ./install
  #cp /home/tests/testscripts/* /home/tests/smoosh-fuzz/tests
#RUN node /home/tests/smoosh-fuzz/src/runTests/checkInstall.js
# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.
