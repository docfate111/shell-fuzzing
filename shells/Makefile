CC=afl-gcc

.PHONY: all clean

all: bin/tcsh bin/zsh bin/yash bin/ksh bin/mksh bin/bash5 bin/bash4 bin/bash3 bin/heirloom-sh bin/osh bin/posh

# MMG 2020-10-05 why --without-tcset-pgrp?
bin/tcsh:
	cd tcsh/src && ./configure --without-tcsetpgrp && $(MAKE) && cp tcsh $@

bin/zsh:
	cd zsh/src && ./configure --without-tcsetpgrp && $(MAKE) && mv zsh $@

bin/yash:
	cd yash/src && ./configure --enable-array --enable-dirstack --enable-help --enable-history --enable-lineedit
	\ --enable-nls --enable-printf --enable-socket --enable-test --enable-ulimit && $(MAKE) && mv yash $@

bin/ksh:
	cd ksh/src && ninja -C build install && mv ksh $@

bin/mksh:
	cd mksh/src && /bin/sh ./Build.sh && mv mksh $@

bin/bash5:
	cd bash5/src && ./configure && $(MAKE) && cp bash $@

bin/bash4:
	cd bash4/src && ./configure && $(MAKE) && cp bash $@

bin/bash3:
	cd bash3/src && ./configure && $(MAKE) && cp bash $@

bin/heirloom-sh:
	cd heirloom-sh/src && $(MAKE) && cp sh $@

bin/osh:
	cd osh/src && ./configure && $(MAKE) && mv osh $@
 
bin/posh:
	cd posh/src && autoreconf -fiv && ./configure --disable-dependency-tracking --disable-silent-rules && $(MAKE) && mv posh $@ 
	
clean:
	-rm -f bin/*



