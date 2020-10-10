CC=afl-gcc

.PHONY: all clean

all: tcsh zsh yash ksh mksh bash5 bash4 bash3 heirloom-sh osh posh

# MMG 2020-10-05 why --without-tcset-pgrp?
tcsh:
	cd tcsh/src && ./configure --without-tcsetpgrp && $(MAKE) && mv tcsh ..

zsh:
	cd zsh/src && ./configure --without-tcsetpgrp && $(MAKE) && mv zsh ..

yash:
	cd yash/src && ./configure --enable-array --enable-dirstack --enable-help --enable-history --enable-lineedit
	\ --enable-nls --enable-printf --enable-socket --enable-test --enable-ulimit && $(MAKE) && mv yash ..

ksh:
	cd ksh/src && ninja -C build install && mv ksh ..

mksh:
	cd mksh/src && /bin/sh ./Build.sh && mv mksh ..

bash5:
	cd bash5/src && ./configure && $(MAKE) && cp bash ../bash5

bash4:
	cd bash4/src && ./configure && $(MAKE) && cp bash ../bash4

bash3:
	cd bash3/src && ./configure && $(MAKE) && cp bash ../bash3

heirloom-sh:
	cd heirloom-sh/src && $(MAKE) && cp sh ../heirloom-sh

osh:
	cd osh/src && ./configure && $(MAKE) && mv osh ..

posh:
	cd posh/src && autoreconf -fiv && ./configure --disable-dependency-tracking --disable-silent-rules && $(MAKE) && mv posh .. 

smoosh: 
	
clean:
	-rm -f tcsh zsh yash ksh mksh bash5 bash4 bash3 heirloom-sh osh posh



