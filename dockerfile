FROM ubuntu
#1. Write a docker that sets up
#   a. random generation script.
RUN "sudo apt install git build-essential libreadline-dev"
RUN "git clone https://github.com/mgree/smoosh-fuzz.git"
RUN "cd smoosh-fuzz/src/posix"
RUN "./generateScripts.sh"
#   b. A bunch of shells. At a minimum:
RUN "sudo apt-add-repository ppa:fish-shell/release-3"
RUN "sudo apt-get update"
#      - dash
#      - yash
#      - ksh
#      - mksh
#      - bosh
#      - zsh
#      - osh
RUN "cd ~"
RUN "git clone https://github.com/oilshell/oil.git"
RUN "git submodule update --init --recursive"
RUN "osh=~/oil/bin/osh
#      - fish
RUN "apt install git bash dash yash ksh mksh bosh zsh fish"
#      - bash (3.x, 4.x, and 5.x)
RUN "git clone https://github.com/MacMiniVault/bash3.2.53.git"
RUN "bash3='/bash3.2.53/bin/bash'"
#bash 4.4
RUN "git clone https://github.com/gitGNU/gnu_bash.git"
RUN "cd gnu_bash"
RUN "./configure"
RUN "make"
RUN "cd .."
#bash 5.0
RUN "git clone https://github.com/errodriguez/bash5.git"
RUN "cd bash5"
RUN "./configure"
RUN "make"
RUN "cd .."
#      - heirloom SH 
RUN "git clone https://github.com/Sunshine-OS/heirloom-sh.git"
RUN "cd heirloom-sh"
RUN "make"
RUN "make install"
RUN "cd -"

# 2. Write a script in the language of your choosing that:
#   a. Reads in a sample script.
#   b. Runs each shell on that script, recording STDOUT, STDERR, exit
#      status, and any changes to the filesystem.
#   c. Outputs a summary comparing the behavior of each shell, grouping
#      them into equivalence classes.
