#!/bin/bash
sudo yum -y install git xz-utils wget autotools-dev automake perl man groff-base cmake libncurses5-dev \
    python3 make python3-pip build-essential sudo libreadline-dev gettext ninja-build autoconf \
    software-properties-common bison flex
pip3 install termcolor gramfuzz
git clone https://github.com/google/AFL.git
cd AFL
make
make install
make clean all
# idk if these packages are needed: yum -y install tzdata asciidoc
# download AFL (TODO: put AFL-fuzz binaries in PATH?)
#cd ~
#cd smoosh-fuzz/src/scriptGeneration
#./generateScripts.sh 100 
# download shells
#mkdir ~/smoosh-fuzz/shells
cd ~/smoosh-fuzz/shells
#  install dash
wget https://dl.bintray.com/homebrew/mirror/dash-0.5.11.2.tar.gz
mkdir dash && tar xf dash-0.5.11.2.tar.gz -C dash --strip-components 1
cd ~/smoosh-fuzz/shells
# download tcsh
wget https://ftp.osuosl.org/pub/blfs/conglomeration/tcsh/tcsh-6.22.02.tar.gz
mkdir -p tcsh/src && tar xf tcsh-6.22.02.tar.gz -C tcsh/src --strip-components 1
cd ~/smoosh-fuzz/shells
# download zsh
wget https://www.zsh.org/pub/zsh-5.8.tar.xz
mkdir -p zsh/src && tar xf zsh-5.8.tar.xz -C zsh/src --strip-components 1
cd ~/smoosh-fuzz/shells
# download yash
wget https://dotsrc.dl.osdn.net/osdn/yash/73097/yash-2.50.tar.xz
mkdir -p yash/src && tar xf yash-2.50.tar.xz -C yash/src --strip-components 1
cd ~/smoosh-fuzz/shells 
# download ksh
wget https://github.com/att/ast/releases/download/2020.0.0/ksh-2020.0.0.tar.gz
mkdir -p ksh/src &&  tar xf ksh-2020.0.0.tar.gz -C ksh/src --strip-components 1
cd ~/smoosh-fuzz/shells
# download mksh
wget https://pub.allbsd.org/MirOS/dist/mir/mksh/mksh-R56.tgz 
mkdir -p mksh/src && tar xf mksh-R56.tgz -C mksh/src --strip-components 1
cd ~/smoosh-fuzz/shells
# download fish: error about fish being slow from afl-fuzz
wget https://github.com/fish-shell/fish-shell/releases/download/3.1.2/fish-3.1.2.tar.gz
mkdir -p fish/src && tar xf fish-3.1.2.tar.gz -C fish/src --strip-components 1
cd ~/smoosh-fuzz/shells
# download bash5
wget https://ftp.gnu.org/gnu/bash/bash-5.0.tar.gz
mkdir -p bash5/src && tar xf bash-5.0.tar.gz -C bash5/src --strip-components 1
cd ~/smoosh-fuzz/shells
# make directory for bash3
mkdir -p bash3/src && tar xf bash-3.2.57.tar.gz -C bash3/src --strip-components 1
cd ~/smoosh-fuzz/shells
# make directory for bash3
mkdir -p bash3/src && tar xf bash-3.2.57.tar.gz -C bash3/src --strip-components 1
cd ~/smoosh-fuzz/shells
# make directory for bash4
mkdir -p bash4/src && tar xf bash-4.0.tar.gz -C bash4/src --strip-components 1
cd ~/smoosh-fuzz/shells
# make directory for heirloom-sh
git clone https://github.com/grml/heirloom-sh
cd heirloom-sh
mkdir src && mv * src
cd ~/smoosh-fuzz/shells
# make directory for oil shell
wget https://www.oilshell.org/download/oil-0.8.0.tar.gz
mkdir -p osh/src && tar xf oil-0.8.0.tar.gz -C osh/src --strip-components 1
rm *gz *xz
cd ~/smoosh-fuzz/shells
# make directory for posh
wget https://salsa.debian.org/clint/posh/-/archive/debian/0.14.1/posh-debian-0.14.1.tar.bz2
mkdir -p posh/src && tar xf posh-debian-0.14.1.tar.bz2 -C posh/src --strip-components 1
cd ~/smoosh-fuzz/shells
rm *bz2
mkdir -p bin
# installing smoosh
git clone --recurse-submodules https://github.com/mgree/smoosh.git
cd smoosh
# # install opam:
# wget https://github.com/ocaml/opam/releases/download/2.0.3/opam-2.0.3-x86_64-linux
# sudo cp opam-2.0.3-x86_64-linux /usr/bin/opam
# sudo chmod +x /usr/bin/opam
#  # get dependency:
# sudo yum install bubblewrap gmp gmp-devel
# opam init
#  opam install -y ocamlfind ocamlbuild num zarith extunix lem
# (afl-gcc?) make -C src all all.byte
# : Package `libdash' not found???
# # installing ninja build system for ksh
# cd ~
# git clone git://github.com/ninja-build/ninja.git && cd ninja
# ./configure.py --bootstrap
# sudo cp ninja /usr/bin/ninja
# # installing meson for ksh:
# sudo pip3 install meson
