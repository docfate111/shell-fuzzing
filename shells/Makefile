CC=$(shell which afl-gcc)

.PHONY: all clean

all: bin/yash bin/ksh bin/mksh bin/bash5 bin/bash4 bin/bash3 bin/heirloom-sh bin/osh bin/posh bin/tcsh bin/zsh

bin/yash:
	cd yash/src && CC="afl-gcc" ./configure --enable-array --enable-dirstack --enable-help --enable-history --enable-lineedit --enable-nls --enable-printf --enable-socket --enable-test --enable-ulimit && CC=afl-gcc $(MAKE) && mv yash ../../$@

# MMG 2020-10-05 why --without-tcset-pgrp?
bin/tcsh:
	cd tcsh/src && CC="afl-gcc" ./configure  && CC=afl-gcc CC=afl-gcc $(MAKE) && mv tcsh ../../$@

bin/bash5:
	cd bash5/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && mv bash ../../$@

bin/bash4:
	cd bash4/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && mv bash ../../$@

bin/bash3:
	cd bash3/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && mv bash ../../$@

bin/heirloom-sh:
	cd heirloom-sh/src && CC=afl-gcc $(MAKE) && mv sh ../../$@

bin/posh:
	cd posh/src && autoreconf -fiv && CC="afl-gcc" ./configure --disable-dependency-tracking --disable-silent-rules && CC=afl-gcc $(MAKE) && mv posh $@ 

# can't install ninja
bin/ksh:
	cd ksh/src && CC="afl-gcc" ninja -C build install && mv ksh ../../$@

# can't find the zsh binary
bin/zsh:
	cd zsh/src && CC="afl-gcc" ./configure  && CC=afl-gcc $(MAKE) && mv zsh ../../$@

# can't find the osh binary
bin/osh:
	cd osh/src && CC="afl-gcc" ./configure && CC=afl-gcc $(MAKE) && mv osh ../../$@

# wget https://pub.allbsd.org/MirOS/dist/mir/mksh/mksh-R59b.tgz and other links gave 404?
bin/mksh:
	cd mksh/src && CC="afl-gcc" /bin/sh ./Build.sh -r && mv mksh ../../$@

clean:
	-rm -f bin/*