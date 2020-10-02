#!/bin/bash
yum -y install git xz-utils wget autotools-dev automake perl man groff-base cmake libncurses5-dev \
    python3 make python3-pip build-essential sudo libreadline-dev gettext ninja-build autoconf
    software-properties-common bison flex
pip3 install termcolor gramfuzz
git clone https://github.com/google/AFL.git
cd AFL
make
make install
make clean all 
#I don't think I need this, maybe later I will change $CC in all the below commands if that is correct
# CC=/usr/local/bin/afl-g++
#CCX=/usr/local/bin/afl-gcc 
# idk if these packages are needed: yum -y install tzdata asciidoc
# download AFL (TODO: put AFL-fuzz binaries in PATH?)
cd ~
git clone https://github.com/mgree/smoosh-fuzz.git
cd smoosh-fuzz/src/scriptGeneration
./generateScripts.sh 100 
# download shells
mkdir ~/shells
cd ~/shells
#  install dash
wget https://dl.bintray.com/homebrew/mirror/dash-0.5.11.2.tar.gz
mkdir dash && tar xf dash-0.5.11.2.tar.gz -C dash --strip-components 1
CC=$(which afl-gcc) ./configure --without-tcsetpgrp  && make && make install
cd ~/shells
# download tcsh
wget https://ftp.osuosl.org/pub/blfs/conglomeration/tcsh/tcsh-6.22.02.tar.gz
mkdir -p tcsh/src && tar xf tcsh-6.22.02.tar.gz -C tcsh/src --strip-components 1
cd ~/shells
# download zsh
wget https://www.zsh.org/pub/zsh-5.8.tar.xz
mkdir -p zsh/src && tar xf zsh-5.8.tar.xz -C zsh/src --strip-components 1
cd ~/shells
# download yash
wget https://dotsrc.dl.osdn.net/osdn/yash/73097/yash-2.50.tar.xz
mkdir -p yash/src && tar xf yash-2.50.tar.xz -C yash/src --strip-components 1
cd ~/shells 
# download ksh
wget https://github.com/att/ast/releases/download/2020.0.0/ksh-2020.0.0.tar.gz
mkdir -p ksh/src &&  tar xf ksh-2020.0.0.tar.gz -C ksh/src --strip-components 1
cd ~/shells
# download mksh
wget https://pub.allbsd.org/MirOS/dist/mir/mksh/mksh-R59b.tgz 
mkdir -p mksh/src && tar xf mksh-R59b.tgz -C mksh/src --strip-components 1
cd ~/shells
# download fish: error about fish being slow from afl-fuzz
wget https://github.com/fish-shell/fish-shell/releases/download/3.1.2/fish-3.1.2.tar.gz
mkdir -p fish/src && tar xf fish-3.1.2.tar.gz -C fish/src --strip-components 1
cd ~/shells
# download bash5
wget https://ftp.gnu.org/gnu/bash/bash-5.0.tar.gz
mkdir -p bash5/src && tar xf bash-5.0.tar.gz -C bash5/src --strip-components 1
cd ~/shells
# WORKDIR /home/smoosh-fuzz/shells
# #      - bash (3.x (MAC) and  4.x)
# RUN tar -xf bash-4.0.tar.gz
#     tar xf bash-3.2.57.tar.gz
#     cd bash-4.0 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  &&  CC=$(which afl-gcc) CCX=$(which afl-g++) make
#     CC=$(which afl-gcc) CCX=$(which afl-g++) make install && cp bash /usr/local/bin/bash4 && cd /home/smoosh-fuzz/shells
#     cd bash-3.2.57 && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  && CC=$(which afl-gcc) CCX=$(which afl-g++) make
#     CC=$(which afl-gcc) CCX=$(which afl-g++) make install && cp bash /usr/local/bin/bash3
# WORKDIR /home/smoosh-fuzz/shells
# #      - heirloom SH
# RUN git clone https://github.com/grml/heirloom-sh
#     cd heirloom-sh/
#       CC=$(which afl-gcc) CCX=$(which afl-g++) make && mv sh /usr/local/bin/heirloom-sh &&  cd /home/smoosh-fuzz/shells
#     tar -x --xz < oil-0.8.pre4.tar.xz
#     cd oil-0.8.pre4
#     CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure  && CC=$(which afl-gcc) CCX=$(which afl-g++) make && ./install \
#     && cd /home/smoosh-fuzz/shells/ && rm *gz *xz
# WORKDIR /home/smoosh-fuzz/shells
# # for some reason this gives an error:
# # maybe later posh shell could be tested
# # RUN apt source posh && cd posh && CC=$(which afl-gcc) CCX=$(which afl-g++) ./configure && make && make install
# WORKDIR /home/smoosh-fuzz/shells
# RUN mkdir -p /home/tests/zshtests && cp -r zsh/Test/* /home/tests/zshtests
#     mkdir -p /home/tests/yashtests &&  cp -r yash/tests/* /home/tests/yashtests 
#     mkdir -p /home/tests/tcshtests &&  cp -r tcsh/tests/* /home/tests/tcshtests 
#     mkdir -p /home/tests/mkshtests && cp -r mksh/test.sh /home/tests/mkshtests
#     mkdir -p /home/tests/fishtests && cp -r fish/tests/* /home/tests/fishtests 
#     mkdir -p /home/tests/bash4tests && cp -r bash-4.0/tests/* /home/tests/bash4tests 
#     mkdir -p /home/tests/bash3tests && cp -r bash-3.2.57/tests/* /home/tests/bash3tests
#     touch ~/.zshrc && mkdir -p /home/tests/results
#     mkdir -p /home/tests/alltests && cp -r yash/tests/* /home/tests/alltests 
#     cp -r zsh/Test/* /home/tests/alltests
#     cp -r yash/tests/* /home/tests/alltests
#     cp -r tcsh/tests/* /home/tests/alltests
#     cp -r mksh/test.sh /home/tests/alltests
#     cp -r fish/tests/* /home/tests/alltests
#     cp -r bash-4.0/tests/* /home/tests/alltests
#     cp -r bash-3.2.57/tests/* /home/tests/alltests
#     python3 /home/smoosh-fuzz/src/runTests/checkInstall.py