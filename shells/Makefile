CC=$(shell which afl-gcc)

.PHONY: all clean

all: bin/yash bin/ksh bin/mksh bin/bash5 bin/bash4 bin/bash3 bin/heirloom-sh bin/osh bin/posh bin/tcsh bin/zsh

# MMG 2020-10-05 why --without-tcset-pgrp?
bin/tcsh:
	cd tcsh/src && CC="afl-gcc" ./configure  && CC=afl-gcc CC=afl-gcc $(MAKE) && cp tcsh ../../$@

bin/zsh:
	cd zsh/src && CC="afl-gcc" ./configure  && CC=afl-gcc $(MAKE) && mv zsh/src/zsh $@

bin/yash:
	cd yash/src && CC="afl-gcc" ./configure --enable-array --enable-dirstack --enable-help --enable-history --enable-lineedit --enable-nls --enable-printf --enable-socket --enable-test --enable-ulimit && CC=afl-gcc $(MAKE) && mv yash ../../bin

bin/ksh:
	cd ksh/src && CC="afl-gcc" ninja -C build install && mv ksh ../../bin

bin/mksh:
	cd mksh/src && CC="afl-gcc" /bin/sh ./Build.sh && mv mksh ../../bin

bin/bash5:
	cd bash5/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && cp bash $@

bin/bash4:
	cd bash4/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && cp bash $@

bin/bash3:
	cd bash3/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && cp bash $@

bin/heirloom-sh:
	cd heirloom-sh/src && CC=afl-gcc $(MAKE) && cp sh $@

bin/osh:
	cd osh/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && mv osh $@

bin/posh:
	cd posh/src && autoreconf -fiv && CC="afl-gcc" ./configure --disable-dependency-tracking --disable-silent-rules && CC=afl-gcc $(MAKE) && mv posh $@ 
	
clean:
	-rm -f bin/*